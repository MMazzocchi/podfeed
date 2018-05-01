''' Module containing parsing classes for podcasts published by Gimlet Media '''

from ..parser import AbstractFeedParser

class GimletParser(AbstractFeedParser):
  ''' Generic parser for podcasts published by Gimlet Media. '''

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href

class EveryLittleThingParser(GimletParser):
  ''' Parser for the Every Little Thing podcast. '''

  NAME = "every_little_thing"
  URL = "http://feeds.gimletmedia.com/eltshow"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class HeavyweightParser(GimletParser):
  ''' Parser for the Heavyweight podcast. '''

  NAME = "heavyweight"
  URL = "http://feeds.gimletmedia.com/heavyweightpodcast"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class ReplyAllParser(GimletParser):
  ''' Parser for the Replay All podcast. '''

  NAME = "reply_all_parser"
  URL = "http://feeds.gimletmedia.com/hearreplyall"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class ScienceVsParser(GimletParser):
  ''' Parser for the Science Vs podcast. '''

  NAME = "science_vs"
  URL = "http://feeds.gimletmedia.com/sciencevs"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class UncivilParser(GimletParser):
  ''' Parser for the Uncivil podcast. '''

  NAME = "uncivil"
  URL = "http://feeds.gimletmedia.com/uncivil"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class SandraParser(GimletParser):
  ''' Parser for the Sandra podcast. '''

  NAME = "sandra"
  URL = "http://feeds.gimletmedia.com/sandrashow"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class TheHabitatParser(GimletParser):
  ''' Parser for The Habitat podcast. '''

  NAME = "the_habitat"
  URL = "http://feeds.gimletmedia.com/thehabitat"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)

class WeCameToWinParser(GimletParser):
  ''' Parser for the We Came To Win podcast. '''

  NAME = "we_came_to_win"
  URL = "http://feeds.gimletmedia.com/wecametowin"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)


