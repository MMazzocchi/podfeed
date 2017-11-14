from urllib.request import urlopen
import re

from .NprMultiPageParser import NprMultiPageParser

class HiddenBrainParser(NprMultiPageParser):
  NAME = "hidden_brain"
  URL = "https://www.npr.org/rss/rss.php?id=423302056"

  def __init__(self):
    NprMultiPageParser.__init__(self, self.NAME, self.URL)
