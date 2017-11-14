from urllib.request import urlopen
import re

from .NprMultiPageParser import NprMultiPageParser

class PlanetMoneyParser(NprMultiPageParser):
  NAME = "planet_money"
  URL = "https://www.npr.org/rss/rss.php?id=93559255"

  def __init__(self):
    NprMultiPageParser.__init__(self, self.NAME, self.URL)
