import tweepy
from config import TWITTER

class TwitterStreamer:

    def __init__(self):
        self.auth = tweepy.OAuthHandler(
            TWITTER['CONSUMER_KEY'],
            TWITTER['CONSUMER_SECRET'],
        )
        self.auth.set_access_token(TWITTER['ACCESS_TOKEN'], TWITTER['ACCESS_SECRET'])
        self.api = tweepy.API(self.auth)


