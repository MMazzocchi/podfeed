Quickstart
==========

Install ``podfeed``: :doc:`installation`

Setup a parser and gather some episodes::

    import time
    import podfeed

    # Get episodes from the last hour
    one_hour_ago = time.time() - (1000*60*60)
    episodes = podfeed.parseFeed("https://www.mypodcast.com/rss/",
                                 one_hour_ago)

    for episode in episodes:
      print("New episode found: {0}, published at {1}".format(
        episode.getTitle(), episode.getDate()))

Next up:
  * Do something with the episode: :doc:`/parsers/episode`
  * Make a playlist: :doc:`/playlists/playlists`
