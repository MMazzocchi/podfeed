Parsers
=======

The ``StandardFeedParser`` is the default parser used when calling
``parseFeed``, and should be enough for most, if not all, RSS feeds.

Upon parsing a feed, the ``StandardFeedParser`` does the following:

  1. Downloads a feed served by the URL.
  2. Parses each entry, excluding those:
  
    a. Without a valid link (:ref:`valid-links`)
    b. Published before the given timestamp
  
  3. For each remaining entry, it creates an ``Episode`` object.

On the rare occasion, a feed will be formatted in a way that doesn't conform to
the format ``podfeed`` expects. In this case, a custom parser can be created by
subclassing the ``StandardFeedParser``: :ref:`custom-parsers`

.. _valid-links:

Valid Links
-----------

.. sidebar:: "links" section

   Just because the RSS feed doesn't have a literal "links" tag, doesn't mean it
   won't have any valid links. Often, links will be present in an "enclosure"
   tag, or under other names. The underlying
   `feedparser <https://github.com/kurtmckee/feedparser>`_ library usually finds
   these and places them into the "links" section.

In order for a link to be considered valid, it must meet the following
requirements:

1. Must be present under a "links" section in the parsed feed entry.
2. Must have an audio extension (mp3, wav, flac, etc.)

.. _custom-parsers:

Custom Parsers
--------------

By default, the standard parser looks for episode links under a "links" section.
This may not always be the case, however. Links may end up in another section,
or under another name. These feeds can still be parsed, but a custom parser is
needed to find the link.

To create a custom parser, subclass ``StandardFeedParser`` and override the
``getTrackLink(self, entry)`` method. In this method, ``entry`` will be a
dictionary parsed from the feed. Once the link is found, it should be returned
as a string. If no link is present, ``None`` should be returned.

An example parser that retrieves a link under "urls" is below::

    import podfeed
    import time

    class CustomParser(StandardFeedParser):
      def getMp3Link(self, entry):
        if ("urls" in entry) and (len(entry.urls) > 0):
          return entry.urls[0]

        else:
          return None

    parser = CustomParser()
    eps = parseFeed("https://mypodcast.com/rss/", time.time() - 1000,
                    parser=parser)
