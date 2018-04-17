from time import time, localtime
SECONDS_PER_DAY = 24*60*60

def getDateThreshold():
  ''' Get the threshold for new episodes. On Tuesday through Friday, this is
      (the current time - 24 hours). On Monday, this is (the current time -
      72 hours). '''
  timestamp = time()
  time_tuple = localtime(timestamp)

  if(time_tuple.tm_wday == 0): # Monday
    return timestamp - (3 * self.SECONDS_PER_DAY)
  else:
    return timestamp - self.SECONDS_PER_DAY
