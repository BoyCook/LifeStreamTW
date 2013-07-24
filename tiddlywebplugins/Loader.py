from twython import Twython
from tiddlyweb.model.tiddler import Tiddler
from config import config


class Loader():
    def __init__(self, store):
        self.store = store

    def load_tweets(self):
        # https://github.com/ryanmcgrath/twython
        print 'Loading tweets...'
        twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
        tweets = twitter.get_user_timeline()
        for tweet in tweets:
            self.add_tiddler(tweet)
        return tweets

    def add_tiddler(self, tweet):
        id_str = tweet['id_str']
        tiddler = Tiddler('Tweet' + id_str, 'tweets')
        tiddler.text = tweet['text']
        tiddler.fields['created_at'] = tweet['created_at']
        tiddler.fields['user_name'] = tweet['user']['screen_name']
        tiddler.modifier = 'LifeStreamDataLoader'
        self.store.put(tiddler)
