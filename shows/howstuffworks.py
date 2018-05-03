''' Module containing parser classes for podcasts published by How Stuff Works
    '''

from ..parser import AbstractFeedParser

class HowStuffWorksParser(AbstractFeedParser):
  ''' Generic parser for podcasts published by How Stuff Works '''

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href

class StuffYouShouldKnowParser(HowStuffWorksParser):
  ''' Parser for the Stuff You Should Know podcast '''

  NAME = "stuff_you_should_know"
  URL = "https://www.howstuffworks.com/podcasts/stuff-you-should-know.rss"

  def __init__(self):
    HowStuffWorksParser.__init__(self, self.NAME, self.URL)

class PartTimeGeniusParser(HowStuffWorksParser):
  ''' Parser for the Part Time Genius podcast '''

  NAME = "part_time_genius"
  URL = "https://www.howstuffworks.com/podcasts/part-time-genius.rss"

  def __init__(self):
    HowStuffWorksParser.__init__(self, self.NAME, self.URL)
