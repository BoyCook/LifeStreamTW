from tiddlyweb.control import filter_tiddlers
from tiddlywebplugins.utils import do_html
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.store import Store
from tiddlyweb.config import config
from tiddlyweb import control
from Loader import Loader
from ScheduledLoad import ScheduledLoad
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('templates'))
SUCCESS_RESPONSE = ['<html><body><h1>Done</h1></body></html>']
MODULES_TO_BAG = {}
MODULES_TO_BAG['titter'] = 'tweets'
MODULES_TO_BAG['wordpress'] = 'blogs'
MODULES_TO_BAG['github'] = 'github'

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
    load_modules = config['lifestream_modules'] 
    store = environ['tiddlyweb.store']
    feed = get_recipe_contents('feed', store, environ)
    tweets = get_bag_contents('tweets', store)
    blogs = get_bag_contents('blogs', store)
    githubs = get_bag_contents('github', store)
    template = template_env.get_template('index.html')
    google_site_verification = config['google_site_verification']
    welcome_file = config['lifestream_welcome_file']
    title = config['lifestream_title']
    header = config['lifestream_header']
    description = config['lifestream_description']
    keywords = config['lifestream_keywords']
    site_image = config['lifestream_site_image']
    return template.generate(welcome=welcome_file,
                             google_site_verification=google_site_verification,
                             title=title,
                             header=header,
                             description=description,
                             keywords=keywords,
                             site_image=site_image,
                             feed=feed,
                             tweets=tweets,
                             blogs=blogs,
                             githubs=githubs)


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
