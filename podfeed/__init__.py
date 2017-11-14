from logging import getLogger, NullHandler
LOGGER = getLogger('podfeed')
LOGGER.addHandler(NullHandler())

__all__ = [
  "crooked",
  "gimlet",
  "npr",
  "other"
]

from .Podfeed import Podfeed
