import feedparser

class AbstractFeedParser:
  def __init__(self, url):
    self.url = url

  def getEpisodesSince(self, date):
    data = feedparser.parse(self.url)

    if data['bozo'] == 1:
      print("ERROR: {0} was not a valid feed: {1}".format(
            self.url, data['bozo_exception']))

    else:
      pass
