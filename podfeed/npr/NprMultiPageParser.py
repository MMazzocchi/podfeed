from urllib.request import urlopen
import re
from logging import getLogger
LOGGER = getLogger("podfeed.NprMultiPageParser")

from ..AbstractFeedParser import AbstractFeedParser

class NprMultiPageParser(AbstractFeedParser):
  MP3_REGEX_STR = "(https://.*mp3)"

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

    self.mp3_regex = re.compile(self.MP3_REGEX_STR)

  def getMp3Link(self, entry):
    page_link = entry['link']
    mp3_link = None

    LOGGER.info("Retrieving page: {0}".format(page_link))

    with urlopen(page_link) as page:
      for line in page:
        results = self.mp3_regex.search(line.decode())

        if results:
          mp3_link = results.group(0)

    if mp3_link:
      return mp3_link

    else:
      raise Exception("Could not find MP3 link!")
