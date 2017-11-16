''' Module containing parser classes for podcasts that don't fit into another
    category. '''

from .AbstractFeedParser import AbstractFeedParser
from .FeedBurnerParser import FeedBurnerParser

class IntelligenceMattersParser(AbstractFeedParser):
  ''' Parser for the Intelligence Matters podcast. '''
  NAME = "intelligence_matters"
  URL = "http://intelligencematters.libsyn.com/rss"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[1].href

class AndThatsWhyWeDrinkParser(AbstractFeedParser):
  ''' Parser for the And That's Why We Drink podcast '''
  NAME = "and_thats_why_we_drink"
  URL = "https://audioboom.com/channels/4911419.rss"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.media_content[0]['url']

class LifeOfTheLawParser(FeedBurnerParser):
  ''' Parser for the Life of the Law podcast '''
  NAME = "life_of_the_law"
  URL = "http://feeds.feedburner.com/LifeOfTheLaw"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class GeointerestingParser(AbstractFeedParser):
  ''' Parser for the Geointeresting podcast '''
  NAME = "geointeresting"
  URL = "http://feeds.soundcloud.com/users/soundcloud:users:149471698/sounds.rss"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[1].href
