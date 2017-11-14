from .CrookedParser import CrookedParser

class LovettOrLeaveItParser(CrookedParser):
  NAME = "LovettOrLeaveIt"
  URL = "http://feeds.feedburner.com/lovett-or-leave-it"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
