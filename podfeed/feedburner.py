from .parser import AbstractFeedParser

class FeedBurnerParser(AbstractFeedParser):
  ''' Generic parser class for podcasts hosted by FeedBurner. '''

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href
