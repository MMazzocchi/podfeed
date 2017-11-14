import feedparser
from time import gmtime, time, mktime
from urllib.request import urlopen
from math import floor

class AbstractFeedParser:
  def __init__(self, name, url, directory):
    self.name = name
    self.url = url
    self.directory = directory

  def saveNewEpisodes(self, date):
    data = feedparser.parse(self.url)

    if data['bozo'] == 1:
     raise data['bozo_exception']
 
    else:
      entries = data['entries']

      for entry in entries:
        self.processEntryIfNew(entry, date)

  def processEntryIfNew(self, entry, date):
    updated = mktime(entry['updated_parsed'])

    if updated >= date:
      filename = self.makeFilename(entry)

      try:
        self.parseAndWrite(entry, filename)

      except Exception as e:
        print("An error occured while parsing an entry. This entry "+
          "will be ignored: {0}".format(e))

  def makeFilename(self, entry):
    time = floor(mktime(entry['updated_parsed']))
    return "{0}/{1}_{2}.mp3".format(self.directory, self.name, time)

  def parseAndWrite(self, entry, filename):
    mp3_link = self.getMp3Link(entry)

    with urlopen(mp3_link) as response:
      self.writeResponseToFile(response, filename)

  def writeResponseToFile(self, response, filename):
    with open(filename, "wb") as outfile:
     print("Writing {0}...".format(filename))

     chunk = response.read(16 * 1024)
     while chunk:
       outfile.write(chunk)
       chunk = response.read(16 * 1024)                

  def getMp3Link(self, entry):
    raise NotImplementedError("AbstractFeedParser.getMp3Link() "+
      "should be overriden for parent classes!")
