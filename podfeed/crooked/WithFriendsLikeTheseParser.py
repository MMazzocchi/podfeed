from .CrookedParser import CrookedParser

class WithFriendsLikeTheseParser(CrookedParser):
  NAME = "with_friends_like_these"
  URL = "http://feeds.feedburner.com/with-friends-like-these"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
