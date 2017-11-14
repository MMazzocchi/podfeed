from time import time, localtime
from logging import getLogger
LOGGER = getLogger("podfeed")

class Podfeed:
  SECONDS_PER_DAY = 24*60*60

  def __init__(self):
    self.parsers = []

  def addParser(self, parser):
    self.parsers.append(parser)

  def collectNewEpisodes(self, directory):
    date = self.getDate()

    LOGGER.info("Collecting episodes posted after {0}, saving to directory {1}"
      .format(date, directory))

    for parser in self.parsers:
      parser.saveNewEpisodes(date, directory)

  def getDate(self):
    timestamp = time()
    time_tuple = localtime(timestamp)

    if(time_tuple.tm_wday == 0): # Monday
      return timestamp - (3 * self.SECONDS_PER_DAY)
    else:
      return timestamp - self.SECONDS_PER_DAY
