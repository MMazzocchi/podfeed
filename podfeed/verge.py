''' Module containing parser classes for podcasts published by The Verge '''

from .FeedBurnerParser import FeedBurnerParser

class WhydYouPushThatButtonParser(FeedBurnerParser):
  ''' Parser for the Why'd You Push That Button podcast. '''

  NAME = "whyd_you_push_that_button"
  URL = "http://feeds.feedburner.com/WhydYouPushThatButton"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class VergecastParser(FeedBurnerParser):
  ''' Parser for the Vergecast podcast. '''

  NAME = "vergecast"
  URL = "http://feeds.feedburner.com/ThisIsMyNextPodcast"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class VergeExtrasParser(FeedBurnerParser):
  ''' Parser for the Verge Extras podcast. '''

  NAME = "verge_extras"
  URL = "http://feeds.podtrac.com/9_7foVqogqP3"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)


