from logging import getLogger, NullHandler
LOGGER = getLogger('podfeed')
LOGGER.addHandler(NullHandler())

from .Podfeed import Podfeed
