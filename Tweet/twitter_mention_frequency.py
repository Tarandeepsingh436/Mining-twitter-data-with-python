from fnmatch import fnmatch
import imp
import json
import sys 
from collections import Counter
import json





"""
we can observe our user mentions 


"""

def get_mentions (tweet):
    entities = tweet.get('entities', {})
    mentions = entities.get('user_mentions', [])
    return [mention['screen_name'] for mention in hashtag]

if __name__ == '__main__':
    fnanme = sys.argv[1]
    with open(fname, 'r') as f:
        users = Counter()
        for line in f: 
            tweet = json.loads(line)
            mentions = get_mentions(tweet)
            users.update(mentions_in__tweet)
        for user, count in users.most_common(20):
            print("{}: {}".format(user, count))







