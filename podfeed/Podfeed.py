from time import time, localtime

class Podfeed:
  SECONDS_PER_DAY = 24*60*60

  def __init__(self):
    self.parsers = []

  def addParser(self, parser):
    self.parsers.append(parser)

  def collectNewEpisodes(self, temp_dir):
    date = self.getDate() 

    for parser in self.parsers:
      parser.saveNewEpisodes(date, temp_dir)

  def getDate(self):
    timestamp = time()
    time_tuple = localtime(timestamp)

    if(time_tuple.tm_wday == 0): # Monday
      return timestamp - (3 * self.SECONDS_PER_DAY)
    else:
      return timestamp - self.SECONDS_PER_DAY
