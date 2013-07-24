from config import config
from twython import Twython


class Loader():
    def load_tweets(self):
        # https://github.com/ryanmcgrath/twython
        print 'Loading tweets...'
        twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
        tweets = twitter.get_user_timeline()
        for tweet in tweets:
            print tweet['text']
        return tweets
