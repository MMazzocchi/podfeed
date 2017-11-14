from logging import getLogger, NullHandler
LOGGER = getLogger('podfeed')
LOGGER.addHandler(NullHandler())
