import feedparser
from time import mktime
from urllib.request import urlopen
from math import floor
from logging import getLogger
LOGGER = getLogger('podfeed')

class Episode:
  ''' Episode represents a single entry in the RSS feed containing a link. '''

  CHUNK_SIZE = 32*1024

  def __init__(self, title, date, link):
    self.title = title
    self.date = date
    self.link = link

  def download(self):
    ''' Download this episode and return it as a request object '''
    return urlopen(self.link)

  def write(self, file_obj):
    ''' Download this episode and write it to the specified object '''

    with self.download() as response:
      try:
        chunk = response.read(self.CHUNK_SIZE)
        while chunk:
          file_obj.write(chunk)
          chunk = response.read(self.CHUNK_SIZE)

      except Exception as err:
        LOGGER.error("Could not write file: {0}".format(err))

  def writeFile(self, path):
    ''' Download this episode and write it to the specified filename '''
    LOGGER.debug("Writing {0}...".format(path))

    with self.download() as response:
      with open(path, 'wb') as outfile:
        self.write(outfile)

  def getLink(self):
    return self.link

  def getTitle(self):
    return self.title

  def getDate(self):
    return self.date

class AbstractFeedParser:
  ''' AbstractFeedParser is a base class used to parse an RSS feed and identify,
      extract, and download MP3 files from it.

      AbstractFeedParser should be subclassed for a specific RSS feed or type of
      feed. '''
  CHUNK_SIZE = 32*1024

  def __init__(self, name, url):
    self.name = name
    self.url = url

  def getNewEpisodes(self, date):
    ''' Gather new episodes for this feed. '''
    LOGGER.debug("Running {0} parser".format(self.name))

    data = feedparser.parse(self.url)

    if self.isValidData(data) == False:
      raise data['bozo_exception']
 
    else:
      entries = data['entries']
      episodes = []

      for entry in entries:
        if self.isNewEntry(entry, date):
          try:
            episode = self.makeEpisode(entry)            
            episodes.append(episode)

          except Exception as e:
            LOGGER.warn("An error occured while parsing an entry for "+
              "{0}. This entry will be ignored: {1}".format(self.name, e))

      LOGGER.debug("Processed {0} entries for {1}".format(len(episodes), self.name))
      return episodes

  def makeEpisode(self, entry):
    ''' Create an Episode object for this entry '''
    time = floor(mktime(entry['updated_parsed']))
    link = self.getMp3Link(entry)

    episode = Episode(self.name, time, link)
    return episode

  def isNewEntry(self, entry, date):
    ''' Return true if this entry was published after the given date. '''
    published = mktime(entry['published_parsed'])
    return published >= date

  def isValidData(self, data):
    ''' Return true if this data is valid (well-formed) '''
    valid = True

    if(data['bozo'] == 1):
      exception = data['bozo_exception']

      # CharacterEncodingOverride indicates there was a mismatch between the
      # encoding specified in the HTTP header, and the encoding specified in the
      # XML. This is actually fine; feedparser can handle it regardless.
      if(isinstance(exception, feedparser.CharacterEncodingOverride)):
        LOGGER.warn("{0} parser returned inconsistently encoded data".format(
          self.name))

      else:
        valid = False 

    return valid

  def getName(self):
    return self.name

  def getMp3Link(self, entry):
    ''' Extract a link to an MP3 file from this entry.
        This method should be overwritten by all child classes. '''
    raise NotImplementedError("AbstractFeedParser.getMp3Link() "+
      "should be overriden for parent classes!")
