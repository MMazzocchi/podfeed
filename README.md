# podfeed
`podfeed` is a python3 package that will read a list of RSS podcast feeds and download the latest ones into a directory.

## Example Usage
```python
from podfeed.parser import parseFeed

# Collect episodes published after May 1st, 2018 
episodes = parseFeed("https://www.npr.org/rss/podcast.php?id=510289", 1525132800)

# Write each episode to a file
for episode in episodes:
  episode.writeFile("./{0}_{1}.mp3".format(
    episode.getTitle(), episode.getDate()))
```

## Logging
`podfeed` uses the built-in python [logging module](https://docs.python.org/3/library/logging.html), using loggers with the top-level name `podfeed`.
