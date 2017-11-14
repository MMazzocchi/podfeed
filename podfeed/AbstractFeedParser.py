import feedparser
from time import gmtime, time, mktime
from urllib.request import urlopen
from math import floor

class AbstractFeedParser:
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
        updated = mktime(entry['updated_parsed'])

        if updated >= date:
          try:
            filename = "{0}/{1}_{2}.mp3".format(
              directory, self.name, floor(updated))

            mp3_link = self.getMp3Link(entry)
            with urlopen(mp3_link) as response:
              with open(filename, "wb") as outfile:
                print("Writing {0}...".format(filename))

                chunk = response.read(16 * 1024)
                while chunk:
                  outfile.write(chunk)
                  chunk = response.read(16 * 1024)                

          except Exception as e:
            print("An error occured while parsing an entry. This entry "+
              "will be ignored: {0}".format(e))

  def getMp3Link(self, entry):
    raise NotImplementedError("AbstractFeedParser.getMp3Link() "+
      "should be overriden for parent classes!")
