from tiddlyweb.model.tiddler import Tiddler
from config import config
from twython import Twython
from wordpress import WordPress


class Loader():
    def __init__(self, store):
        self.store = store
        self.twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
        self.wp = WordPress('', cache=None)

    def load_tweets(self):
        # https://github.com/ryanmcgrath/twython
        print 'Loading tweets...'

        tweets = self.twitter.get_user_timeline()
        for tweet in tweets:
            self.add_tweet_tiddler(tweet)
        return tweets

    def load_blog_posts(self):
        # https://github.com/eyeseast/python-wordpress
        self.wp.get_recent_posts()

    def add_tweet_tiddler(self, tweet):
        id_str = tweet['id_str']
        tiddler = Tiddler('Tweet' + id_str, 'tweets')
        tiddler.text = tweet['text']
        tiddler.fields['created_at'] = tweet['created_at']
        tiddler.fields['user_name'] = tweet['user']['screen_name']
        tiddler.modifier = 'LifeStreamDataLoader'
        self.store.put(tiddler)
