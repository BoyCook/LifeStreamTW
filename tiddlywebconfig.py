# A basic configuration.
# `pydoc tiddlyweb.config` for details on configuration items.
import mangler

config = {
    'system_plugins': ['tiddlywebplugins.lifestream', 'tiddlywebplugins.static'],
    'secret': '150d9eabe2bd925c536ef4451afe3c345cebdb2b',
    'twanager_plugins': ['tiddlywebwiki'],
    'google_site_verification': 'cgE8_AF7n-I1t-6pn4fEJzLW01HVdGzfsGVCfi7hyDs',
    'lifestream_modules': ['twitter', 'wordpress', 'github'],
    'lifestream_welcome_file': 'welcome.html',
	'lifestream_title': 'Craig Cook on the web [beta]',
	'lifestream_header': 'Craig Cook',
    'lifestream_description': 'Craig Cook on the web',
    'lifestream_keywords': 'Craig Cook developer software engineer',
    'lifestream_site_image': 'static/images/craig.jpg',
	'static_url_dir': 'static',
	'static_file_dir': './static',    
    'log_level': 'DEBUG',
}
