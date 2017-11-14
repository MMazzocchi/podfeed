from .CrookedParser import CrookedParser

class PodSaveAmericaParser(CrookedParser):
  NAME = "pod_save_america"
  URL = "http://feeds.feedburner.com/pod-save-america"

  def __init__(self):
    CrookedParser.__init__(self, self.NAME, self.URL)
