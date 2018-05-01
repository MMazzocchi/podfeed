''' Module containing parsing classes for podcasts published by NASA. '''
from ..parser import AbstractFeedParser

class NasaParser(AbstractFeedParser):
  ''' Generic class for parsing NASA published podcasts. '''

  def __init__(self, url, name):
    AbstractFeedParser.__init__(self, url, name)

  def getMp3Link(self, entry):
    return entry.links[1].href

class GravityAssistParser(NasaParser):
  ''' Parser for the Gravity Assist podcast '''
  NAME = "gravity_assist"
  URL = "https://www.nasa.gov/rss/dyn/Gravity-Assist.rss"

  def __init__(self):
    NasaParser.__init__(self, self.NAME, self.URL)

class HoustonWeHaveAPodcastParser(NasaParser):
  ''' Parser for the Houston, We Have A Podcast podcast '''
  NAME = "houston_we_have_a_podcast"
  URL = "https://www.nasa.gov/rss/dyn/Houston-We-Have-a-Podcast.rss"

  def __init__(self):
    NasaParser.__init__(self, self.NAME, self.URL)
