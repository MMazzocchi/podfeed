''' Module for parsers associated with podcasts published by NPR. '''

from urllib.request import urlopen
import re
from logging import getLogger

from .AbstractFeedParser import AbstractFeedParser

class WaitWaitDontTellMeParser(AbstractFeedParser):
  ''' Parser for the Wait, Wait, Don't Tell Me podcast '''

  NAME = "wait_wait_dont_tell_me"
  URL = "https://www.npr.org/rss/podcast.php?id=344098539"

  def __init__(self):
    AbstractFeedParser.__init__(self, self.NAME, self.URL)

  def getMp3Link(self, entry):
    return entry.links[0].href

class NprMultiPageParser(AbstractFeedParser):
  ''' Parser for any NPR podcast that requires multiple page requests.

      Some NPR podcasts do not have links to an MP3 file in their RSS feed 
      entries. Instead, they have links to specific NPR web pages, which contain
      the download link.

      This parser will extract the page link from an entry, then search that
      page for a link to an MP3.
  '''

  LOGGER = getLogger("podfeed.NprMultiPageParser")
  MP3_REGEX_STR = "(https://.*mp3)"

  def __init__(self, name, url):
    AbstractFeedParser.__init__(self, name, url)

    self.mp3_regex = re.compile(self.MP3_REGEX_STR)

  def getMp3Link(self, entry):
    page_link = entry['link']
    mp3_link = None

    self.LOGGER.debug("Retrieving page: {0}".format(page_link))

    with urlopen(page_link) as page:
      for line in page:
        results = self.mp3_regex.search(line.decode())

        if results:
          mp3_link = results.group(0)

    if mp3_link:
      return mp3_link

    else:
      raise Exception("Could not find MP3 link!")

class HiddenBrainParser(NprMultiPageParser):
  ''' Parser for the Hidden Brain podcast. '''

  NAME = "hidden_brain"
  URL = "https://www.npr.org/rss/rss.php?id=423302056"

  def __init__(self):
    NprMultiPageParser.__init__(self, self.NAME, self.URL)

class PlanetMoneyParser(NprMultiPageParser):
  ''' Parser for the Planet Money podcast. '''

  NAME = "planet_money"
  URL = "https://www.npr.org/rss/rss.php?id=93559255"

  def __init__(self):
    NprMultiPageParser.__init__(self, self.NAME, self.URL)
