#!/usr/bin/env python

import unittest
from tiddlywebplugins.Loader import Loader

class LoaderTest(unittest.TestCase):
    def setUp(self):
        self.loader = Loader(None)

    def test_load_tweets(self):
        self.loader.load_tweets()

    def test_load_tweets(self):
        self.loader.load_blog_posts()

    def test_load_tweets(self):
        self.loader.load_github()

if __name__ == '__main__':
    unittest.main()
