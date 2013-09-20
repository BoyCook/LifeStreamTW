from tiddlyweb.model.bag import Bag
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.control import filter_tiddlers
from tiddlyweb.store import Store
from tiddlyweb.config import config
from tiddlyweb import control
from jinja2 import Environment, FileSystemLoader

class MyLifestream():
	MODULE_CONFIG = {
		'twitter': ['tweet', 'Tweets', 'icon-twitter'],
		'wordpress': ['blog', 'Blog', 'icon-wordpress'],
		'github': ['github', 'GitHub', 'icon-github'],
		'linkedin': ['linkedin', 'LinkedIn', 'icon-linkedin'],
		'jenkins': 	['jenkins', 'Jenkins', 'icon-cog'],
		'flickr': ['flickr', 'Flickr', 'icon-flickr']
	}
	template_env = Environment(loader=FileSystemLoader('templates'))

	def __init__(self, modules, store, environ):
		self.set_modules(modules)
		self.store = store
		self.environ = environ
		# TODO make some of these optional
		self.twitter_user = config['twitter_user']
		self.google_site_verification = config['google_site_verification']
		self.welcome_file = config['lifestream_welcome_file']
		self.title = config['lifestream_title']
		self.header = config['lifestream_header']
		self.description = config['lifestream_description']
		self.keywords = config['lifestream_keywords']
		self.site_image = config['lifestream_site_image']
		
	def get_home(self):
		feed = self.get_recipe_contents('feed', self.store, self.environ)
		tweets = self.get_bag_contents('tweets', self.store)
		blogs = self.get_bag_contents('blogs', self.store)
		githubs = self.get_bag_contents('github', self.store)
		template = self.template_env.get_template('index.html')
		return template.generate(welcome=self.welcome_file,
                         google_site_verification=self.google_site_verification,
                         twitter_user=self.twitter_user,
                         title=self.title,
                         header=self.header,
                         description=self.description,
                         keywords=self.keywords,
                         site_image=self.site_image,
                         modules=self.modules,
                         feed=feed,
                         tweets=tweets,
                         blogs=blogs,
                         githubs=githubs)

	def get_recipe_contents(self, recipe_name, store, env):
	    recipe = Recipe(recipe_name)
	    recipe = self.store.get(recipe)
	    tiddlers = self.populate_tiddlers(control.get_tiddlers_from_recipe(recipe, env), store)
	    return self.sort_tiddlers(tiddlers)

	def get_bag_contents(self, bag_name, store):
	    bag = Bag(bag_name)
	    bag = self.store.get(bag)
	    tiddlers = self.populate_tiddlers(store.list_bag_tiddlers(bag), store)
	    return self.sort_tiddlers(tiddlers)

	def populate_tiddlers(self, tiddlers, store):
	    tiddlers = list(tiddlers)
	    # TODO loop backwards so don't have to reverse later
	    for i, tiddler in enumerate(tiddlers):
	        tiddlers[i] = self.store.get(tiddler)
	    return tiddlers

	def sort_tiddlers(self, tiddlers):
	    return filter_tiddlers(tiddlers, 'sort=-sort_field')		

	def set_modules(self, modules):
		self.modules = [];
		for module in modules:
			self.modules.append(self.MODULE_CONFIG.get(module))
