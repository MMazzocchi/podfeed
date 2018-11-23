import unittest
import time
from logging import getLogger, StreamHandler

from .server import ServerThread

from podfeed.parser import validTrackLink, isNewEntry, StandardFeedParser

VALID_LINK="track.mp3"
INVALID_LINK="track.jpg"

NOW = time.mktime(time.localtime())
NEW = time.localtime(NOW+1000)
OLD = time.localtime(NOW-1000)

NEW_ENTRY = { "published_parsed": NEW }
OLD_ENTRY = { "published_parsed": OLD }

PORT = 8080
URL = "http://localhost:{0}/test/data/".format(PORT)

NOV_23 = time.mktime(time.strptime("Thu Nov 23 00:00:00 2018"))

LOGGER = getLogger("podfeed")
#LOGGER.addHandler(StreamHandler())

class UtilsTests(unittest.TestCase):
  def test_validTrackLink(self):
    self.assertTrue(validTrackLink(VALID_LINK))
    self.assertFalse(validTrackLink(INVALID_LINK))

  def test_isNewEntry(self):
    self.assertTrue(isNewEntry(NEW_ENTRY, NOW))
    self.assertFalse(isNewEntry(OLD_ENTRY, NOW))

class FeedParserTests(unittest.TestCase):
  def setUp(self):
    self.server_thread = ServerThread(PORT)

  def test_getNewEpisodes(self):
    parser = StandardFeedParser(URL+"/valid")
    eps = parser.getNewEpisodes(NOV_23)
    self.assertIs(len(eps), 1)

  def test_getNewEpisodesTooEarly(self):
    parser = StandardFeedParser(URL+"/too_early")
    eps = parser.getNewEpisodes(NOV_23)
    self.assertIs(len(eps), 0)

  def test_getNewEpisodesNoLink(self):
    parser = StandardFeedParser(URL+"/no_link")
    eps = parser.getNewEpisodes(NOV_23)
    self.assertIs(len(eps), 0)

  def test_getNewEpisodesNonMp3(self):
    parser = StandardFeedParser(URL+"/non_mp3")
    eps = parser.getNewEpisodes(NOV_23)
    self.assertIs(len(eps), 0)

  def tearDown(self):
    self.server_thread.stop()

if __name__ == "__main__":
  unittest.main()
