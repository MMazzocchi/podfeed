# podfeed
`podfeed` is a python3 package that will read a list of RSS podcast feeds and download the latest ones into a directory.

## Example Usage
```python
from podfeed import Podfeed
from podfeed.npr import PlanetMoneyParser

podfeed = Podfeed()

# Add the parser for Planet Money
podfeed.addParser(PlanetMoneyParser())

# Collect any new episodes and place in the directory ./episodes
podfeed.collectNewEpisodes("./episodes")
```

## Logging
`podfeed` uses the built-in python [logging module](https://docs.python.org/3/library/logging.html), using loggers with the to-level name `podfeed`. Add a handler to see logging output.
