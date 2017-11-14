from time import time, localtime
from logging import getLogger
LOGGER = getLogger("podfeed")

class Podfeed:
  ''' Collection of RSS feed parsers that can download recent episodes in MP3
      format and save them into a directory. '''
  SECONDS_PER_DAY = 24*60*60

  def __init__(self):
    self.parsers = []

  def addParser(self, parser):
    ''' Add a parser to the collection. '''
    self.parsers.append(parser)

  def collectNewEpisodes(self, directory):
    ''' Collect all new episodes from all parsers and save them into the given
        directory. '''
    date = self.getDate()

    LOGGER.info("Collecting episodes posted after {0}, saving to directory {1}"
      .format(date, directory))

    for parser in self.parsers:
      parser.saveNewEpisodes(date, directory)

  def getDate(self):
    ''' Get the threshold for new episodes. On Tuesday through Friday, this is
        (the current time - 24 hours). On Monday, this is (the current time -
        72 hours). '''
    timestamp = time()
    time_tuple = localtime(timestamp)

    if(time_tuple.tm_wday == 0): # Monday
      return timestamp - (3 * self.SECONDS_PER_DAY)
    else:
      return timestamp - self.SECONDS_PER_DAY
