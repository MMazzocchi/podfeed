import feedparser
from time import gmtime, time, mktime
from urllib.request import urlopen
from math import floor

class AbstractFeedParser:
  CHUNK_SIZE = 32*1024

  def __init__(self, name, url):
    self.name = name
    self.url = url

  def saveNewEpisodes(self, date, directory):
    data = feedparser.parse(self.url)

    if data['bozo'] == 1:
     raise data['bozo_exception']
 
    else:
      entries = data['entries']

      for entry in entries:
        if self.isNewEntry(entry, date):
          self.processEntry(entry, directory)

  def isNewEntry(self, entry, date):
    updated = mktime(entry['updated_parsed'])
    return updated >= date

  def processEntry(self, entry, directory):
    filename = self.makeFilename(entry, directory)

    try:
      mp3_link = self.getMp3Link(entry)
      with urlopen(mp3_link) as response:
        self.writeResponseToFile(response, filename)

    except Exception as e:
      print("An error occured while parsing an entry. This entry "+
        "will be ignored: {0}".format(e))

  def makeFilename(self, entry, directory):
    time = floor(mktime(entry['updated_parsed']))
    return "{0}/{1}_{2}.mp3".format(directory, self.name, time)

  def writeResponseToFile(self, response, filename):
    with open(filename, "wb") as outfile:
      print("Writing {0}...".format(filename))

      chunk = response.read(self.CHUNK_SIZE)
      while chunk:
        outfile.write(chunk)
        chunk = response.read(self.CHUNK_SIZE)                

  def getMp3Link(self, entry):
    raise NotImplementedError("AbstractFeedParser.getMp3Link() "+
      "should be overriden for parent classes!")
