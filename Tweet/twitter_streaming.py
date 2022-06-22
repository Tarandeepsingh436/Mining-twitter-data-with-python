"""
Streaming API
"""
import sys
import os 
import time 
import string
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitter_client import get_twitter_auth

class CustomListener(StreamListener):   # helper to sanitize the query and use it for the filename.
  """Custom StreamListener for streaming Twitter data."""

  def __init__(self, fname):
    safe_fname = format_filename(fname)
    self.outfile = "stream_%s.jsonl" % safe_fname


  def on_data(self, data):
# This function simply stores the data as it is received in a .jsonl file.
    try:
      with open(self.outfile, 'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      sys.stderr.write("Error on_data: {}\n".format(e))
      time.sleep(5)
    return True



  def on_error(self, status):   # in particular will deal with explicit errors from Twitter.
    if status == 420:
      sys.stderr.write("Rate limit exceeded\n")
      return False
    else:
      sys.stderr.write("Error {}\n".format(status))
      return True

  def format_filename(fname):
    """
    convert fname into a safe string for a file name
    """
    return ''.join(convert)






























