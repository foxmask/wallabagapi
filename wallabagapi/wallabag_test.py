# coding: utf-8
"""
   Wallabag API - Test
"""

import datetime
import unittest
from unittest import IsolatedAsyncioTestCase
from wallabagapi.core import WallabagAPI


class TestWallabag(IsolatedAsyncioTestCase):

    host = 'http://wallabag:81'
    client_id = ''
    client_secret = ''
    token = ''

    async def asyncSetUp(self):

        params = {"grant_type": "password",
                  "client_id": '1_3847efhvxack8gwog8scg8oowww0csogg4wwoogg0cg444g8k4',
                  "client_secret": 'i1j19n9e7mog0ook48gwo0kck88oskggwgswwg48gsw4sc8gk',
                  "username": 'wallabag',
                  "password": 'wallabag'}

        self.token = await WallabagAPI.get_token(host=self.host, **params)
        self.format = 'json'
        self.w = WallabagAPI(host=self.host, token=self.token)

    async def test_get_token(self):
        params = {"grant_type": "password",
                  "client_id": '1_3847efhvxack8gwog8scg8oowww0csogg4wwoogg0cg444g8k4',
                  "client_secret": 'i1j19n9e7mog0ook48gwo0kck88oskggwgswwg48gsw4sc8gk',
                  "username": 'wallabag',
                  "password": 'wallabag'}
        data = await WallabagAPI.get_token(host=self.host, **params)
        self.assertTrue(isinstance(data, str), True)
        return data

    async def create_entry(self):
        self.format = 'json'

        url = 'https://somwhereelse.over.the.raibow.com/'
        kwargs = dict()
        kwargs['title'] = 'the FooBar Title'
        kwargs['tags'] = ['foo', 'bar']
        kwargs['starred'] = 0
        kwargs['archive'] = 0
        kwargs['content'] = '<p>Additional content</p>'
        kwargs['language'] = 'FR'
        kwargs['published_at'] = datetime.datetime.now()
        kwargs['authors'] = 'John Doe'
        kwargs['public'] = 0
        kwargs['original_url'] = 'http://localhost'
        data = await self.w.post_entries(url, **kwargs)

        return data

    async def test_get_entries(self):
        params = {'delete': 0,
                  'sort': 'created',
                  'order': 'desc',
                  'page': 1,
                  'perPage': 30,
                  'tags': []}
        data = await self.w.get_entries(**params)
        self.assertIsInstance(data, dict)

    async def test_get_entry(self):
        entry = await self.create_entry()
        new_id = entry['id']
        self.assertTrue(isinstance(new_id, int), True)
        data = await self.w.get_entry(new_id)
        self.assertTrue(data, str)

    async def test_get_entry_tags(self):
        entry = await self.create_entry()
        new_id = entry['id']
        self.assertTrue(isinstance(new_id, int), True)
        data = await self.w.get_entry_tags(new_id)
        self.assertIsInstance(data, list)

    async def test_get_tags(self):
        data = await self.w.get_tags()
        self.assertIsInstance(data, list)

    async def test_post_entries(self):
        data = await self.create_entry()
        self.assertTrue(data, True)

    async def test_patch_entries(self):
        entry = await self.create_entry()
        new_id = entry['id']
        params = {'title': 'I change the title',
                  'archive': 0,
                  'tags': ["bimbo", "pipo"],
                  'order': 'asc',
                  'star': 0,
                  'delete': 0}
        self.assertTrue(isinstance(new_id, int), True)
        self.assertTrue(isinstance(params, dict), True)
        data = await self.w.patch_entries(new_id, **params)
        self.assertTrue(data, True)

    async def test_delete_entries(self):
        entry = await self.create_entry()
        self.assertTrue(isinstance(entry['id'], int), True)
        data = await self.w.delete_entries(entry['id'])
        self.assertTrue(data, True)

    async def test_post_entry_tags(self):
        entry = await self.create_entry()
        new_id = entry['id']
        self.assertTrue(isinstance(new_id, int), True)
        tags = ['foo', 'bar']
        self.assertTrue(isinstance(tags, list), True)
        data = await self.w.post_entry_tags(new_id, tags)
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
