from tiddlywebplugins.utils import do_html
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.store import Store
from config import config
from twython import Twython
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('templates'))

@do_html()
def home_page(environ, start_response):
    store = environ['tiddlyweb.store']
    tweets = get_bag_contents(store, 'tweets')
    blogs = get_bag_contents(store, 'blogs')
    template = template_env.get_template('index.html')
    return template.generate(tweets=tweets, blogs=blogs)


def init(config):
    selector = config['selector']
    replace_handler(selector, '/', GET=home_page)
    selector.add('/load', GET=load)


def get_bag_contents(store, bag_name):
    bag = Bag(bag_name)
    bag = store.get(bag)
    tiddlers = store.list_bag_tiddlers(bag)
    tiddlers = list(tiddlers)
    for i, tiddler in enumerate(tiddlers):
        tiddlers[i] = store.get(tiddler)
    return tiddlers


def load(environ, start_response):
    load_tweets()
    return '<h1>Done</h1>'


def load_tweets():
    # https://github.com/ryanmcgrath/twython
    print 'Loading tweets...'
    twitter = Twython(config['app_key'], config['app_secret'], config['oauth_token'], config['oauth_token_secret'])
    tweets = twitter.get_user_timeline()
    for tweet in tweets:
        print tweet['text']


