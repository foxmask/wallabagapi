# -*- coding: utf-8 -*-
import unittest
from wallabag import Wallabag


class TestWallabag(unittest.TestCase):

    def setUp(self):
        self.host = "http://localhost:5000"
        self.api_key = '12334567890'
        self.user_agent = 'WallabagPython/1.0 +https://github.com/foxmask/wallabag-api'
        self.format = 'json'

    def test_get_entries(self):
        params = {'archive': 0,
                  'star': 0,
                  'delete': 0,
                  'sort': 'created',
                  'order': 'desc',
                  'page': 1,
                  'perPage': 30,
                  'tags': []}
        w = Wallabag(self.host).get_entries('ABCD', **params)
        self.assertIsInstance(w, dict)

    def test_post_entries(self):
        title = 'foobar title'
        url = ['http://foobar.com/', 'http://barfoo.com/']
        tags = ['foo', 'bar']
        self.assertTrue(isinstance(title, str), True)
        self.assertTrue(isinstance(tags, list), True)
        w = Wallabag(self.host).post_entries('ABCD', url, title, tags)
        self.assertTrue(w, True)

    def test_get_entry(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        w = Wallabag(self.host).get_entry('ABCD', entry)
        self.assertTrue(w, str)

    def test_patch_entries(self):
        entry = 1
        params = {'title': '',
                  'archive': 0,
                  'tags': [],
                  'star': 0,
                  'delete': 0}
        self.assertTrue(isinstance(entry, int), True)
        self.assertTrue(isinstance(params, dict), True)
        w = Wallabag(self.host).patch_entries('ABCD', entry, **params)
        self.assertTrue(w, True)

    def test_delete_entries(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        w = Wallabag(self.host).delete_entries('ABCD', entry)
        self.assertTrue(w, True)

    def test_get_entry_tags(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        w = Wallabag(self.host).get_entry_tags('ABCD', entry)
        self.assertIsInstance(w, list)

    def test_post_entry_tags(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        tags = ['foo', 'bar']
        self.assertTrue(isinstance(tags, list), True)
        w = Wallabag(self.host).post_entry_tags('ABCD', entry, tags)
        self.assertTrue(w, True)

    def test_delete_entry_tag(self):
        entry = 1
        tag = 'tag1'
        self.assertTrue(isinstance(entry, int), True)
        self.assertTrue(isinstance(tag, str), True)
        w = Wallabag(self.host).delete_entry_tag('ABCD', entry, tag)
        self.assertTrue(w, True)

    def test_get_tags(self):
        w = Wallabag(self.host).get_tags('ABCD')
        self.assertTrue(w, True)

    def test_get_tag(self):
        tag = 'tag1'
        self.assertTrue(isinstance(tag, str), True)
        w = Wallabag(self.host).get_tag('ABCD', tag)
        self.assertTrue(w, True)

    def test_delete_tag(self):
        tag = 'tag1'
        self.assertTrue(isinstance(tag, str), True)
        w = Wallabag(self.host).delete_tag('ABCD', tag)
        self.assertTrue(w, True)

if __name__ == '__main__':
    unittest.main()