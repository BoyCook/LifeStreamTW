from tiddlywebplugins.utils import do_html, entitle, require_any_user
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.web.util import get_route_value
from jinja2 import Environment, FileSystemLoader

template_env = Environment(loader=FileSystemLoader('templates'))

@do_html()
def home_page(environ, start_response):
	template = template_env.get_template('index.html')
	return template.generate()

def init(config):
	selector = config['selector']
	replace_handler(selector, '/', GET=home_page)
  	