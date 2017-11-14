import feedparser

class Reader:
  def __init__(self):
    self.urls = []

  def addUrl(self, url):
    self.urls.append(url)

  def addUrls(self, urls):
    self.urls.extend(urls)

  def clearUrls(self):
    self.urls.clear()

  def getFilesSince(self, date):
    pass 
