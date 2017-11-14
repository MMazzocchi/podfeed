from .CrookedParser import CrookedParser

class PodSaveThePeopleParser(CrookedParser):
  NAME = "pod_save_the_people"
  URL = "http://feeds.feedburner.com/pod-save-the-people"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
