from urllib.request import urlopen
import re

from ..AbstractFeedParser import AbstractFeedParser

class CrookedParser(AbstractFeedParser):
  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href
