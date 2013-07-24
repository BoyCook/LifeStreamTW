from config import config
from twython import Twython
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.tiddler import Tiddler

class Loader():

    def __init__(self, store):
        self.store = store

    def load_tweets(self):
        # https://github.com/ryanmcgrath/twython
        print 'Loading tweets...'
        twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
        tweets = twitter.get_user_timeline()
        for tweet in tweets:
            print tweet['user']['screen_name'] + ' - ' + tweet['id_str'] + ' - ' + tweet['created_at'] + ' - ' + tweet['text'] + ' - ' + tweet['text']
        return tweets


    def build_tiddler(self, title, text):
        tiddler = Tiddler(title, 'tweets')
        tiddler.text = text

        tiddler.modifier = 'LifeStreamDataLoader'

    def add_tiddler(self, tiddler):
        self.store.put(tiddler)
