Episode Objects
===============

``Episode`` objects represent a single episode parsed from an RSS feed. They do
not contain an actual audio file; rather, they contain a link to the file
itself. An ``Episode`` can be downloaded using its member methods, or 
placed into a playlist: :doc:`/playlists/playlists`

.. autoclass:: podfeed.parser.Episode
   :members:
