from .AbstractFeedParser import AbstractFeedParser

class HiddenBrainParser(AbstractFeedParser):
  URL = "https://www.npr.org/rss/rss.php?id=423302056"

  def __init__(self):
    AbstractFeedParser.__init__(self, "")
