"""
Analyzing tweets -entity analysis 
analyzing entiites in tweets




"""

import sys
from collections import Counter
import json


def get_hashtag(tweet):   #to extract a list of hashtags.
     entities = tweet.get('entities', {})
     hashtags = entities.get('hashtags', [])
     return [tag['text'].lower() for tag in hashtags]
   




if __name__ == '__main__':
     fname = sys.argv[1]
     with open(fname, 'r') as f:
       hashtags = Counter()

       for line in f:
         tweet = json.loads(line)
         hashtags_in_tweet = get_hashtags(tweet)
         hashtags.update(hashtags_in_tweet)
         
       for tag, count in hashtags.most_common(20):

         print("{}: {}".format(tag, count))










































