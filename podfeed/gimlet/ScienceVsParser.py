from .GimletParser import GimletParser

class ScienceVsParser(GimletParser):
  NAME = "science_vs"
  URL = "http://feeds.gimletmedia.com/sciencevs"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
