from .GimletParser import GimletParser

class EveryLittleThingParser(GimletParser):
  NAME = "every_little_thing"
  URL = "http://feeds.gimletmedia.com/eltshow"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
