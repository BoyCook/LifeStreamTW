from tiddlywebplugins.utils import do_html
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.control import filter_tiddlers
from tiddlyweb.store import Store
from tiddlyweb.config import config
from tiddlyweb import control
from Loader import Loader
from ScheduledLoad import ScheduledLoad
from MyLifestream import MyLifestream

SUCCESS_RESPONSE = ['<html><body><h1>Done</h1></body></html>']

def init(init_config):
    print 'Life Stream init...'
    selector = init_config['selector']
    replace_handler(selector, '/', GET=home_page)
    selector.add('/loadall', GET=load_all)
    selector.add('/loadtweets', GET=load_tweets)
    selector.add('/loadblogs', GET=load_blogs)
    selector.add('/loadgithub', GET=load_github)
    store = Store(config['server_store'][0], config['server_store'][1], environ={'tiddlyweb.config': config})
    scheduledLoad = ScheduledLoad(store)
    scheduledLoad.load()
    

@do_html()
def home_page(environ, start_response):
    store = environ['tiddlyweb.store']
    lifestream = MyLifestream(config['lifestream_modules'], store, environ)
    return lifestream.get_home()


def get_recipe_contents(recipe_name, store, env):
    recipe = Recipe(recipe_name)
    recipe = store.get(recipe)
    tiddlers = populate_tiddlers(control.get_tiddlers_from_recipe(recipe, env), store)
    return sort_tiddlers(tiddlers)


def get_bag_contents(bag_name, store):
    bag = Bag(bag_name)
    bag = store.get(bag)
    tiddlers = populate_tiddlers(store.list_bag_tiddlers(bag), store)
    return sort_tiddlers(tiddlers)


def populate_tiddlers(tiddlers, store):
    tiddlers = list(tiddlers)
    # TODO loop backwards so don't have to reverse later
    for i, tiddler in enumerate(tiddlers):
        tiddlers[i] = store.get(tiddler)
    return tiddlers


def sort_tiddlers(tiddlers):
    return filter_tiddlers(tiddlers, 'sort=-sort_field')


def load_all(environ, start_response):
    store = environ['tiddlyweb.store']
    loader = Loader(store)
    loader.load_all()
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return SUCCESS_RESPONSE


def load_tweets(environ, start_response):
    store = environ['tiddlyweb.store']
    loader = Loader(store)
    loader.load_tweets()
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return SUCCESS_RESPONSE


def load_blogs(environ, start_response):
    store = environ['tiddlyweb.store']
    loader = Loader(store)
    loader.load_blog_posts()
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return SUCCESS_RESPONSE


def load_github(environ, start_response):
    store = environ['tiddlyweb.store']
    loader = Loader(store)
    loader.load_github()
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return SUCCESS_RESPONSE
