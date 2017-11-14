import feedparser
from time import gmtime, time, mktime
from urllib.request import urlopen
from math import floor
from logging import getLogger
LOGGER = getLogger('podfeed')

class AbstractFeedParser:
  CHUNK_SIZE = 32*1024

  def __init__(self, name, url):
    self.name = name
    self.url = url

  def saveNewEpisodes(self, date, directory):
    LOGGER.info("Running {0} parser...".format(self.name))

    data = feedparser.parse(self.url)

    if data['bozo'] == 1:
     raise data['bozo_exception']
 
    else:
      entries = data['entries']
      processed = 0

      for entry in entries:
        if self.isNewEntry(entry, date):
          try:
            self.processEntry(entry, directory)
            processed += 1

          except Exception as e:
            LOGGER.warn("An error occured while parsing an entry. This entry "+
              "will be ignored: {0}".format(e))

      LOGGER.info("Processed {0} entries".format(processed))

  def isNewEntry(self, entry, date):
    updated = mktime(entry['updated_parsed'])
    return updated >= date

  def processEntry(self, entry, directory):
    filename = self.makeFilename(entry, directory)

    mp3_link = self.getMp3Link(entry)
    with urlopen(mp3_link) as response:
      self.writeResponseToFile(response, filename)

  def makeFilename(self, entry, directory):
    time = floor(mktime(entry['updated_parsed']))
    return "{0}/{1}_{2}.mp3".format(directory, self.name, time)

  def writeResponseToFile(self, response, filename):
    with open(filename, "wb") as outfile:
      LOGGER.info("Writing {0}...".format(filename))

      chunk = response.read(self.CHUNK_SIZE)
      while chunk:
        outfile.write(chunk)
        chunk = response.read(self.CHUNK_SIZE)                

  def getMp3Link(self, entry):
    raise NotImplementedError("AbstractFeedParser.getMp3Link() "+
      "should be overriden for parent classes!")
