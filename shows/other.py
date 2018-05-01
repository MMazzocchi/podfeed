''' Module containing parser classes for podcasts that don't fit into another
    category. '''

from ..parser import AbstractFeedParser
from .feedburner import FeedBurnerParser

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
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[1].href

class RevisionistHistoryParser(FeedBurnerParser):
  ''' Parser for the Revisionist History podcast '''
  NAME = "revisionist_history"
  URL = "http://feeds.feedburner.com/RevisionistHistory"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class FreakonomicsRadioParser(FeedBurnerParser):
  ''' Parser for the Freakonomics Radio podcast '''
  NAME = "freakonomics_radio"
  URL = "http://feeds.feedburner.com/freakonomicsradio"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class CriminalParser(FeedBurnerParser):
  ''' Parser for the Criminal podcast '''
  NAME = "criminal"
  URL = "http://feeds.thisiscriminal.com/CriminalShow"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class MythsAndLegendsParser(AbstractFeedParser):
  ''' Parser for the Myths and Legends podcast '''
  NAME = "myths_and_lengends"
  URL = "http://mythpodcast.libsyn.com/rss"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[0].href

class IrlParser(AbstractFeedParser):
  ''' Parser for the IRL podcast by Mozilla '''
  NAME = "irl"
  URL = "https://feeds.mozilla-podcasts.org/irl"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[1].href
