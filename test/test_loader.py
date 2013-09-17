#!/usr/bin/env python

import unittest
from tiddlyweb.store import Store
from tiddlyweb.config import config
from tiddlywebplugins.Loader import Loader


class LoaderTest(unittest.TestCase):
    def setUp(self):
        store = Store(config['server_store'][0],
                      config['server_store'][1],
                      environ={'tiddlyweb.config': config})
        self.loader = Loader(store)

    def test_load_tweets(self):
        self.loader.load_tweets()

    def test_load_tweets(self):
        self.loader.load_blog_posts()

    def test_load_tweets(self):
        self.loader.load_github()


if __name__ == '__main__':
    unittest.main()
