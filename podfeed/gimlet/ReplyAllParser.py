from .GimletParser import GimletParser

class ReplyAllParser(GimletParser):
  NAME = "reply_all_parser"
  URL = "http://feeds.gimletmedia.com/hearreplyall"

  def __init__(self):
    GimletParser.__init__(self, self.NAME, self.URL)
