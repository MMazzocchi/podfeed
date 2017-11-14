from urllib.request import urlopen
import re

from .AbstractFeedParser import AbstractFeedParser

class WaitWaitDontTellMeParser(AbstractFeedParser):
  NAME = "wait_wait_dont_tell_me"
  URL = "https://www.npr.org/rss/podcast.php?id=344098539"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[0].href
