from .CrookedParser import CrookedParser

class CrookedConversationsParser(CrookedParser):
  NAME = "crooked_conversations"
  URL = "http://feeds.feedburner.com/crooked-conversations"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
