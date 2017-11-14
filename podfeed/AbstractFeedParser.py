import feedparser
from time import gmtime, time, mktime

class AbstractFeedParser:
  def __init__(self, name, url):
    self.name = name
    self.url = url

  def getEpisodesSince(self, date):
    data = feedparser.parse(self.url)

    if data['bozo'] == 1:
     raise data['bozo_exception']
 
    else:
      entries = data['entries']

      for entry in entries:
        updated = mktime(entry['updated_parsed'])

        if updated >= date:
          try:
            with self.getMp3File(entry) as mp3_file:
              pass

          except Exception as e:
            print("An error occured while parsing an entry. This entry "+
              "will be ignored: {0}".format(e))

  def getMp3File(self, entry):
    raise NotImplementedError("AbstractFeedParser.getMp3File() "+
      "should be overriden for parent classes!")
