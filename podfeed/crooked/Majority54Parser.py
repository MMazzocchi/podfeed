from .CrookedParser import CrookedParser

class Majority54Parser(CrookedParser):
  NAME = "majority_54"
  URL = "http://feeds.feedburner.com/majority-54"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
