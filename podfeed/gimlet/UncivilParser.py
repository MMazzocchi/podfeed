from .GimletParser import GimletParser

class UncivilParser(GimletParser):
  NAME = "uncivil"
  URL = "http://feeds.gimletmedia.com/uncivil"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
