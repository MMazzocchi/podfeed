class Playlist:
  ''' Represents a playlist of podcast episodes '''

  def __init__(self):
    self.episodes = []

  def addEpisode(self, episode):
    self.episodes.append(episode)

  def addEpisodes(self, episodes):
    self.episodes.extend(episodes)

  def saveAsM3U(self, path):
    with open(path, 'w') as outfile:
      for episode in self.episodes:
        outfile.write("# {0}\n".format(episode.getTitle()))
        outfile.write(episode.getLink())
        outfile.write("\n")
