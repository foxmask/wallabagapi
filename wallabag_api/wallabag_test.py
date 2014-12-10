# -*- coding: utf-8 -*-
import unittest
from wallabag import Wallabag


class TestWallabag(unittest.TestCase):

    def setUp(self):
        self.host = "http://localhost:5000"
        self.api_key = '12334567890'
        self.user = 'foxmask'

    def test_get(self):
        w = Wallabag(self.host).get('ABCD', self.user)
        self.assertIsInstance(w, dict)

    def test_get_entries(self):
        w = Wallabag(self.host).get('ABCD', self.user)
        self.assertIsInstance(w, dict)

    def test_get_entry(self):
        w = Wallabag(self.host).get_entry('ABCD', self.user, 1)
        self.assertTrue(w, str)

    def test_post_entries(self):
        url = ['http://foobar.com/', 'http://barfoo.com/']
        tags = ['foo', 'bar']
        w = Wallabag(self.host).post_entries('ABCD', self.user, url, tags)
        self.assertTrue(w, True)

    def test_patch_entries(self):
        entry = []
        entry.append('fourth content')
        entry.append('fifth content')
        w = Wallabag(self.host).patch_entries('ABCD', self.user, entry)
        self.assertTrue(w, True)

    def test_delete_entry(self):
        entry = 1
        w = Wallabag(self.host).delete_entry('ABCD', self.user, entry)
        self.assertTrue(w, True)

if __name__ == '__main__':
    unittest.main()