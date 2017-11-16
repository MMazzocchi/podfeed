''' Module containing parser classes for podcasts published by Crooked Media.
    '''

from .FeedBurnerParser import FeedBurnerParser

class CrookedConversationsParser(FeedBurnerParser):
  ''' Parser for the Crooked Conversations podcast. '''

  NAME = "crooked_conversations"
  URL = "http://feeds.feedburner.com/crooked-conversations"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class LovettOrLeaveItParser(FeedBurnerParser):
  ''' Parser for the Lovett or Leave It podcast. '''

  NAME = "lovett_or_leave_it"
  URL = "http://feeds.feedburner.com/lovett-or-leave-it"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class Majority54Parser(FeedBurnerParser):
  ''' Parser for the Majority 54 podcast. '''

  NAME = "majority_54"
  URL = "http://feeds.feedburner.com/majority-54"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class PodSaveAmericaParser(FeedBurnerParser):
  ''' Parser for the Pod Save America podcast. '''

  NAME = "pod_save_america"
  URL = "http://feeds.feedburner.com/pod-save-america"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class PodSaveThePeopleParser(FeedBurnerParser):
  ''' Parser for the Pod Save the People podcast. '''

  NAME = "pod_save_the_people"
  URL = "http://feeds.feedburner.com/pod-save-the-people"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class PodSaveTheWorldParser(FeedBurnerParser):
  ''' Parser for the Pod Save the World podcast. '''

  NAME = "pod_save_the_world"
  URL = "http://feeds.feedburner.com/pod-save-the-world"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)

class WithFriendsLikeTheseParser(FeedBurnerParser):
  ''' Parser for the With Friends Like These podcast. '''

  NAME = "with_friends_like_these"
  URL = "http://feeds.feedburner.com/with-friends-like-these"

  def __init__(self):
    FeedBurnerParser.__init__(self, self.NAME, self.URL)
