import os
from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    namespace_packages=['tiddlywebplugins'],
    name='tiddlywebplugins.lifestream',
    version=VERSION,
    description='LifeStream plugin for social services integration',
    long_description=file(os.path.join(os.path.dirname(__file__), 'README')).read(),
    author='Craig Cook',
    url='http://pypi.python.org/pypi/lifestream',
    packages=find_packages(exclude=['test']),
    author_email='boycook@osmosoft.com',
    platforms='Posix; MacOS X; Windows',
    install_requires=['tiddlyweb'],
    zip_safe=False,
)
