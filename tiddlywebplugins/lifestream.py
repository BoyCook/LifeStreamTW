from tiddlywebplugins.utils import do_html
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.model.bag import Bag
from tiddlyweb import control
from Loader import Loader
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('templates'))


@do_html()
def home_page(environ, start_response):
    store = environ['tiddlyweb.store']
    feed = get_recipe_contents('feed', store, environ)
    tweets = get_bag_contents('tweets', store)
    blogs = get_bag_contents('blogs', store)
    githubs = get_bag_contents('github', store)
    template = template_env.get_template('index.html')
    return template.generate(feed=feed, tweets=tweets, blogs=blogs, githubs=githubs)


def init(config):
    selector = config['selector']
    replace_handler(selector, '/', GET=home_page)
    selector.add('/load', GET=load)


def get_recipe_contents(recipe_name, store, env):
    recipe = Recipe(recipe_name)
    recipe = store.get(recipe)
    return populate_tiddlers(control.get_tiddlers_from_recipe(recipe, env), store)


def get_bag_contents(bag_name, store):
    bag = Bag(bag_name)
    bag = store.get(bag)
    return populate_tiddlers(store.list_bag_tiddlers(bag), store)


def populate_tiddlers(tiddlers, store):
    tiddlers = list(tiddlers)
    for i, tiddler in enumerate(tiddlers):
        tiddlers[i] = store.get(tiddler)
    return tiddlers


def load(environ, start_response):
    store = environ['tiddlyweb.store']
    loader = Loader(store)
    loader.load()
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return ['<html><body><h1>Done</h1></body></html>']

