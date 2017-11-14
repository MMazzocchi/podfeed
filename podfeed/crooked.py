''' Module containing parser classes for podcasts published by Crooked Media.
    '''

from .AbstractFeedParser import AbstractFeedParser

class CrookedParser(AbstractFeedParser):
  ''' Generic parser class for podcasts published by Crooked Media. '''

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

  def getMp3Link(self, entry):
    return entry.links[0].href

class CrookedConversationsParser(CrookedParser):
  ''' Parser for the Crooked Conversations podcast. '''

  NAME = "crooked_conversations"
  URL = "http://feeds.feedburner.com/crooked-conversations"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class LovettOrLeaveItParser(CrookedParser):
  ''' Parser for the Lovett or Leave It podcast. '''

  NAME = "lovett_or_leave_it"
  URL = "http://feeds.feedburner.com/lovett-or-leave-it"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class Majority54Parser(CrookedParser):
  ''' Parser for the Majority 54 podcast. '''

  NAME = "majority_54"
  URL = "http://feeds.feedburner.com/majority-54"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class PodSaveAmericaParser(CrookedParser):
  ''' Parser for the Pod Save America podcast. '''

  NAME = "pod_save_america"
  URL = "http://feeds.feedburner.com/pod-save-america"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class PodSaveThePeopleParser(CrookedParser):
  ''' Parser for the Pod Save the People podcast. '''

  NAME = "pod_save_the_people"
  URL = "http://feeds.feedburner.com/pod-save-the-people"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class PodSaveTheWorldParser(CrookedParser):
  ''' Parser for the Pod Save the World podcast. '''

  NAME = "pod_save_the_world"
  URL = "http://feeds.feedburner.com/pod-save-the-world"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)

class WithFriendsLikeTheseParser(CrookedParser):
  ''' Parser for the With Friends Like These podcast. '''

  NAME = "with_friends_like_these"
  URL = "http://feeds.feedburner.com/with-friends-like-these"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
