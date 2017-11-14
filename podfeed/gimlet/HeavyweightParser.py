from .GimletParser import GimletParser

class HeavyweightParser(GimletParser):
  NAME = "heavyweight"
  URL = "http://feeds.gimletmedia.com/heavyweightpodcast"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
