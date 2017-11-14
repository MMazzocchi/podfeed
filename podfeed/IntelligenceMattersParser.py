from urllib.request import urlopen
import re

from .AbstractFeedParser import AbstractFeedParser

class IntelligenceMattersParser(AbstractFeedParser):
  NAME = "intelligence_matters"
  URL = "http://intelligencematters.libsyn.com/rss"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[1].href
