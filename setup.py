import os
from setuptools import setup, find_packages

readme = open('README.md').read()
VERSION = '0.0.1'

REQUIREMENTS = {
    'install': ['httplib2', 'simplejson', 'tiddlyweb', 'tiddlywebplugins.static'],
    'testing': ['pytest', 'coverage', 'pytest-cov', 'python-coveralls'],
}

if __name__ == '__main__':
    setup(
        namespace_packages=['tiddlywebplugins'],
        name='tiddlywebplugins.lifestream',
        version=VERSION,
        description='LifeStream plugin for social services integration',
        long_description=readme,
        author='Craig Cook',
        author_email='boycook@osmosoft.com',
        url='https://github.com/BoyCook/LifeStreamTW',
        packages=find_packages(exclude=['test']),
        # packages=['tiddlywebplugins', 'static', 'templates', 'load'],
        install_requires=REQUIREMENTS["install"],
        extras_require= { "testing":  REQUIREMENTS["testing"] },
        platforms='Posix; MacOS X; Windows',
        zip_safe=False
    )
