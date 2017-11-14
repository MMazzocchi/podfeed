from .AbstractFeedParser import AbstractFeedParser

class GimletParser(AbstractFeedParser):
  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href

class EveryLittleThingParser(GimletParser):
  NAME = "every_little_thing"
  URL = "http://feeds.gimletmedia.com/eltshow"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class HeavyweightParser(GimletParser):
  NAME = "heavyweight"
  URL = "http://feeds.gimletmedia.com/heavyweightpodcast"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class ReplyAllParser(GimletParser):
  NAME = "reply_all_parser"
  URL = "http://feeds.gimletmedia.com/hearreplyall"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class ScienceVsParser(GimletParser):
  NAME = "science_vs"
  URL = "http://feeds.gimletmedia.com/sciencevs"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class UncivilParser(GimletParser):
  NAME = "uncivil"
  URL = "http://feeds.gimletmedia.com/uncivil"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
