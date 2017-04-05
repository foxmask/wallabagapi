# coding: utf-8
import unittest
from wallabag import Wallabag


class TestWallabag(unittest.TestCase):

    host = 'http://localhost:8000'
    client_id = ''
    client_secret = ''
    token = ''

    def setUp(self):
        access_token = self.test_get_token()
        self.format = 'json'
        self.w = Wallabag(host=self.host,
                          token=access_token,
                          client_id=self.client_id,
                          client_secret=self.client_secret)

    def test_get_token(self):
        params = {"grant_type": "password",
                  "client_id":
                  '1_4wqe1riwt0qoks844kwc4go08koogkgk88go4cckkwg0408kcg',
                  "client_secret": '4mzw3qwi1xyc0cks4k80s4c8kco40wwkkkw0g40kwk4o4c44co',
                  "username": 'wallabag',
                  "password": 'wallabag'}
        print(self.host)
        data = Wallabag.get_token(host=self.host, **params)
        print(data)
        self.assertTrue(isinstance(data, str), True)
        return data

    def create_entry(self):
        title = 'foobar title'
        url = 'https://smcomm.trigger-happy.eu/'
        tags = ['foo', 'bar']
        starred = 0
        archive = 0
        data = self.w.post_entries(url, title, tags, starred, archive)
        return data

    def test_get_entries(self):
        params = {'archive': 0,
                  'star': 0,
                  'delete': 0,
                  'sort': 'created',
                  'order': 'desc',
                  'page': 1,
                  'perPage': 30,
                  'tags': []}
        data = self.w.get_entries(**params)
        self.assertIsInstance(data, dict)

    def test_get_entry(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        data = self.w.get_entry(entry)
        self.assertTrue(data, str)

    def test_get_entry_tags(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        data = self.w.get_entry_tags(entry)
        self.assertIsInstance(data, list)

    def test_get_tags(self):
        data = self.w.get_tags()
        self.assertIsInstance(data, list)

    def test_post_entries(self):
        data = self.create_entry()
        self.assertTrue(data, True)

    def test_patch_entries(self):
        entry = 1
        params = {'title': 'I change the title',
                  'archive': 0,
                  'tags': ["bimbo", "pipo"],
                  'order': 'asc',
                  'star': 0,
                  'delete': 0}
        self.assertTrue(isinstance(entry, int), True)
        self.assertTrue(isinstance(params, dict), True)
        data = self.w.patch_entries(entry, **params)
        self.assertTrue(data, True)

    def test_delete_entries(self):
        entry = self.create_entry()
        self.assertTrue(isinstance(entry['id'], int), True)
        data = self.w.delete_entries(entry['id'])
        self.assertTrue(data, True)

    def test_post_entry_tags(self):
        entry = 1
        self.assertTrue(isinstance(entry, int), True)
        tags = ['foo', 'bar']
        self.assertTrue(isinstance(tags, list), True)
        data = self.w.post_entry_tags(entry, tags)
        self.assertTrue(data, True)

    """
    def test_delete_entry_tag(self):
        entry = self.create_entry()
        tag = 'bar'
        self.assertTrue(isinstance(entry['id'], int), True)
        self.assertTrue(isinstance(tag, str), True)
        resp = self.w.delete_entry_tag(entry['id'], tag)
        self.assertTrue(resp, True)
    """

if __name__ == '__main__':
    unittest.main()
