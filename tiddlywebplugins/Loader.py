from tiddlyweb.model.tiddler import Tiddler
from config import config
from twython import Twython
from wordpress.wordpress import WordPress


class Loader():
    def __init__(self, store):
        self.store = store
        self.twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
        self.wp = WordPress('boycook.wordpress.com')

    def load(self):
        self.load_tweets()
        self.load_blog_posts()

    def load_tweets(self):
        print 'Loading tweets...'
        tweets = self.twitter.get_user_timeline()
        for tweet in tweets:
            self.add_tweet_tiddler(tweet)
        return tweets

    def load_blog_posts(self):
        print 'Loading blog posts...'
        posts = self.wp.get_posts()
        for post in posts:
            self.add_blog_post_tiddler(post)

    def add_tweet_tiddler(self, tweet):
        id_str = tweet['id_str']
        tiddler = Tiddler('Tweet' + id_str, 'tweets')
        tiddler.text = tweet['text']
        tiddler.fields['sort_field'] = tweet['created_at']
        tiddler.fields['created_at'] = tweet['created_at']
        tiddler.fields['user_name'] = tweet['user']['screen_name']
        tiddler.modifier = 'LifeStreamDataLoader'
        self.store.put(tiddler)

    def add_blog_post_tiddler(self, post):
        id = str(post['ID'])
        tiddler = Tiddler('Blog' + id, 'blogs')
        tiddler.text = post['content']
        tiddler.fields['sort_field'] = post['modified']
        tiddler.fields['created_at'] = post['date']
        tiddler.fields['modified'] = post['modified']
        tiddler.fields['excerpt'] = post['excerpt']
        tiddler.fields['post_title'] = post['title']
        tiddler.fields['post_url'] = post['URL']
        tiddler.modifier = 'LifeStreamDataLoader'
        self.store.put(tiddler)
