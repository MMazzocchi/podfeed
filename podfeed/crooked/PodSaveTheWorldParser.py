from .CrookedParser import CrookedParser

class PodSaveTheWorldParser(CrookedParser):
  NAME = "pod_save_the_world"
  URL = "http://feeds.feedburner.com/pod-save-the-world"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
