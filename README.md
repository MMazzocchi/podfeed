# podfeed
`podfeed` is a python3 package that will read a list of RSS podcast feeds and download the latest ones into a directory.

## Example Usage
```python
from podfeed.showsnpr import PlanetMoneyParser

# Create a parser
parser = PlanetMoneyParser()

# Collect episodes published after May 1st, 2018 
episodes = podfeed.getNewEpisodes(1525132800)

# Write each to a file
for episode in episodes:
  episode.writeFile("./{0}_{1}.mp3".format(
    episode.getTitle(), episode.getDate()))
```

## Logging
`podfeed` uses the built-in python [logging module](https://docs.python.org/3/library/logging.html), using loggers with the top-level name `podfeed`.
