'''
one that 
       - reads the environment variables and performs the authentication,
and 
       - the other that creates the API object needed to interface with Twitter:
'''

import os 
import sys
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_auth():  #can be used for streaming API

    # peroform the authentication
    """ Setup Twitter oAuth
        Return :tweepy.oauth obj """

    try:
     consumer_key = os.environ['gra9LwzUX4Aa0LfGyhtP6CtHC']
     consumer_secret = os.environ['yWFR0KHOvTAHpF5uwage9MtNi5lppaE3cS9Zf2UmmFJD8moOzg']       
     access_token = os.environ['1301675652433809408-hrqK8eKvVxZvIYdsSWFTbZEwliM6Xc']
     acees_secret = os.environ['FjpNQiz4ZwmPnIX2ZoyJcD2Kq8DSUKrsd3IYfz63pwOqT']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,acees_secret)

    return auth






def get_twitter_client():  #used to create an instance tweepy.API
    """
    setup twitter client
    return : tweety.api object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client





