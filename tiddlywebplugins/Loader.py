from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.store import NoTiddlerError
from config import config
from twython import Twython
from wordpress.wordpress import WordPress
from github import Github


class Loader():
    def __init__(self, store):
        self.store = store
        self.twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'],
                               config['oauth_token_secret'])
        self.wp = WordPress('boycook.wordpress.com')
        self.gitHub = Github()

    def load(self):
        print 'Loading from all sources...'
        self.load_tweets()
        self.load_blog_posts()
        self.load_github()
        print 'Done loading'

    def load_tweets(self):
        tweets = self.twitter.get_user_timeline()
        for tweet in tweets:
            self.add_tweet_tiddler(tweet)
        return tweets

    def load_blog_posts(self):
        posts = self.wp.get_posts()
        for post in posts:
            self.add_blog_post_tiddler(post)

    def load_github(self):
        user = self.gitHub.get_user('BoyCook')
        repos = user.get_repos()
        gists = user.get_gists()
        for repo in repos:
            self.add_github_repo_tiddler(repo)
        for gist in gists:
            self.add_github_gist_tiddler(gist)

    def add_tweet_tiddler(self, tweet):
        id_str = tweet['id_str']
        tiddler = Tiddler('Tweet' + id_str, 'tweets')
        tiddler.text = tweet['text']
        tiddler.tags = ['tweet']
        tiddler.fields['sort_field'] = tweet['created_at']
        tiddler.fields['created_at'] = tweet['created_at']
        tiddler.fields['user_name'] = tweet['user']['screen_name']
        tiddler.fields['item_summary'] = tweet['text']
        tiddler.fields['item_url'] = 'http://twitter.com/BoyCook/status/' + id_str
        tiddler.modifier = 'LifeStreamDataLoader'
        update = self.do_update(tiddler)
        if update:
            self.store.put(tiddler)

    def add_blog_post_tiddler(self, post):
        tiddler = Tiddler('Blog' + str(post['ID']), 'blogs')
        tiddler.text = post['content']
        tiddler.tags = ['blogPost']
        tiddler.fields['sort_field'] = post['modified']
        tiddler.fields['created_at'] = post['date']
        tiddler.fields['modified'] = post['modified']
        tiddler.fields['item_summary'] = post['excerpt']
        tiddler.fields['post_title'] = post['title']
        tiddler.fields['item_url'] = post['URL']
        tiddler.modifier = 'LifeStreamDataLoader'
        update = self.do_update(tiddler)
        if update:
            self.store.put(tiddler)

    def add_github_repo_tiddler(self, repo):
        tiddler = Tiddler('GitHubRepo' + str(repo.id), 'github')
        tiddler.text = repo.name
        tiddler.tags = ['gitHubRepo']
        tiddler.fields['sort_field'] = repo.pushed_at
        tiddler.fields['created_at'] = repo.created_at
        tiddler.fields['updated_at'] = repo.updated_at
        tiddler.fields['item_summary'] = repo.description
        tiddler.fields['item_url'] = repo.html_url
        tiddler.modifier = 'LifeStreamDataLoader'
        update = self.do_update(tiddler)
        if update:
            self.store.put(tiddler)

    def add_github_gist_tiddler(self, repo):
        tiddler = Tiddler('GitHubGist' + str(repo.id), 'github')
        tiddler.text = repo.description
        tiddler.tags = ['gitHubGist']
        tiddler.fields['sort_field'] = repo.updated_at
        tiddler.fields['created_at'] = repo.created_at
        tiddler.fields['updated_at'] = repo.updated_at
        tiddler.fields['item_summary'] = repo.description
        tiddler.fields['item_url'] = repo.html_url
        tiddler.modifier = 'LifeStreamDataLoader'
        update = self.do_update(tiddler)
        if update:
            self.store.put(tiddler)

    def do_update(self, tiddler):
        existing = self.get_tiddler(tiddler)
        if existing is None:
            return True
        elif existing.fields['sort_field'] != tiddler.fields['sort_field']:
            return True
        else:
            return False

    def get_tiddler(self, tiddler):
        try:
            return self.store.get(tiddler)
        except (NoTiddlerError), exc:
            return None
