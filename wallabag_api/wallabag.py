# -*- coding: utf-8 -*-
import requests
import logging

__author__ = 'foxmask'


logging.basicConfig(format='%(message)s', level=logging.INFO)

__all__ = ['Wallabag']


class Wallabag(object):
    """
        Python Class 'Wallabag' to deal with Wallabagap REST API
        This class is able to handle any data from your Wallabagap account
    """

    host = ''
    api_key = ''
    user_agent = ''
    format = ''

    def __init__(self,
                 host='http://v2.wallabag.org',
                 api_key='',
                 extension='json',
                 user_agent="WallabagPython/1.0 +https://github.com/foxmask/wallabag-api"):
        """
            init variable
            :param host: string url to the official API Wallabagap
            :param api_key: string of the key provided by Wallabagap
            :param extension: json/xml/html
            :param user_agent
        """
        self.host = host
        self.api_key = api_key
        self.format = extension
        self.user_agent = user_agent

    def get_host(self):
        """
            get the host from which to get API
            :return host
        """
        return self.host

    def query(self, url, params={}, method='get'):
        """
            Do a query to the System API
            :param url: url to the API
            :param params: a dict with all the necessary things to query the API
            :return json data
        """
        # params = params
        params['key'] = self.api_key
        if method == 'get':
            r = requests.get(self.get_host() + url, params=params)
        elif method == 'post':
            r = requests.post(self.get_host() + url, params=params)
        elif method == 'patch':
            r = requests.patch(self.get_host() + url, params=params)
        elif method == 'delete':
            r = requests.delete(self.get_host() + url, params=params)
        #todo : handle case of self.ext is xml or html
        return self.handle_json_response(r)


    def handle_json_response(self, responses):
        """
            get the json data response
            :param responses: the json response
            :return the json data without 'root' node
        """
        if responses.status_code != 200:
            raise Exception("Wrong status code: ", responses.status_code)
        json_data = {}
        try:
            json_data = responses.json()
        except:
            for error in json_data['errors']:
                logging.error("Wallabag: %s" %
                              json_data['errors'][error]['content'])
        return json_data

    def get_entries(self, token, **kwargs):
        """

            GET /api/entries.{_format}

            Retrieve all entries. It could be filtered by many options.

            :param token: the token that identified the user to access the API
            :param kwargs: can contain one of the following filters
                archive:  '0' or '1', default '0' filter by archived status.
                star: '0' or '1', default '0' filter by starred status.
                delete: '0' or '1', default '0' filter by deleted status.
                sort: 'created' or 'updated', default 'created'
                order: 'asc' or 'desc', default 'desc'
                page: int default 1 what page you want
                perPage: int default 30 result per page
                tags: list of tags url encoded. Will returns entries that matches ALL tags
            :return data related to the ext
        """
        # default values
        params = {'token': token,
                  'archive': 0,
                  'star': 0,
                  'delete': 0,
                  'sort': 'created',
                  'order': 'desc',
                  'page': 1,
                  'perPage': 30,
                  'tags': []}

        if 'archive' in kwargs and int(kwargs['archive']) in (0, 1):
            params['archive'] = int(kwargs['archive'])
        if 'star' in kwargs and int(kwargs['star']) in (0, 1):
            params['star'] = int(kwargs['star'])
        if 'delete' in kwargs and int(kwargs['delete']) in (0, 1):
            params['delete'] = int(kwargs['delete'])
        if 'order' in kwargs and kwargs['order'] in ('asc', 'desc'):
            params['order'] = kwargs['order']
        if 'page' in kwargs and isinstance(kwargs['page'], int):
            params['page'] = kwargs['page']
        if 'perPage' in kwargs and isinstance(kwargs['perPage'], int):
            params['perPage'] = kwargs['perPage']
        if 'tags' in kwargs and isinstance(kwargs['tags'], list):
            params['tags'] = kwargs['tags']

        url = '/api/entries.{ext}'.format(ext=self.format)

        return self.query(url, params, method="get")

    def post_entries(self, token, url, title='', tags=[]):
        """

            POST /api/entries.{_format}

            Create an entry

            :param token: the token that identified the user to access the API
            :param url: the url of the note to store
            :param title: Optional, we'll get the title from the page.
            :param tags: tag1,tag2,tag3 a comma-separated list of tags.
            :return result
        """
        params = {'token': token, 'url': url, 'title': title, 'tags': []}
        if len(tags) > 0 and isinstance(tags, list):
            params['tags'] = tags
        url = '/api/entries.{ext}'.format(ext=self.format)
        return self.query(url, params, method="post")

    def get_entry(self, token, entry):
        """

            GET /api/entries/{entry}.{_format}

            Retrieve a single entry

            :param token: the token that identified the user to access the API
            :param entry: \w+ an integer The Entry ID
            :return data related to the ext
        """
        params = {'token': token}
        url = '/api/entries/{entry}.{ext}'.format(entry=entry, ext=self.format)
        return self.query(url, params, method="get")

    def patch_entries(self, token, entry, **kwargs):
        """

            PATCH /api/entries/{entry}.{_format}

            Change several properties of an entry

            :param token: the token that identified the user to access the API
            :param entry: the entry to 'patch' / update
            :param kwargs: can contain one of the following
                title: string
                tags: a list of tags tag1,tag2,tag3
                archive:  '0' or '1', default '0' archived the entry.
                star: '0' or '1', default '0' starred the entry
                delete: '0' or '1', default '0' flag as deleted. In case that you don't want to *really* remove it..
            :return data related to the ext
        """
        # default values
        params = {'token': token,
                  'title': '',
                  'archive': 0,
                  'tags': [],
                  'star': 0,
                  'delete': 0}
        if 'title' in kwargs:
            params['title'] = kwargs['title']
        if 'tags' in kwargs and isinstance(kwargs['tags'], list):
            params['tags'] = kwargs['tags']
        if 'archive' in kwargs and int(kwargs['archive']) in (0, 1):
            params['archive'] = int(kwargs['archive'])
        if 'star' in kwargs and int(kwargs['star']) in (0, 1):
            params['star'] = int(kwargs['star'])
        if 'delete' in kwargs and int(kwargs['delete']) in (0, 1):
            params['delete'] = int(kwargs['delete'])

        url = '/api/entries/{entry}.{ext}'.format(entry=entry, ext=self.format)
        return self.query(url, params, method="patch")


    def delete_entries(self, token, entry):
        """

            DELETE /api/entries/{entry}.{_format}

            Delete permanently an entry

            :param token: the token that identified the user to access the API
            :param entry: \w+ an integer The Entry ID
            :return result
        """
        params = {'token': token}
        url = '/api/entries/{entry}.{ext}'.format(entry=entry, ext=self.format)
        return self.query(url, params, method="delete")

    def get_entry_tags(self, token, entry):
        """

            GET /api/entries/{entry}/tags.{_format}

            Retrieve all tags for an entry

            :param token: the token that identified the user to access the API
            :param entry: \w+ an integer The Entry ID
            :return data related to the ext
        """
        params = {'token': token}
        url = '/api/entries/{entry}/tags.{ext}'.format(entry=entry, ext=self.format)
        return self.query(url, params, method="get")

    def post_entry_tags(self, token, entry):
        """

            POST /api/entries/{entry}/tags.{_format}

            Add one or more tags to an entry

            :param token: the token that identified the user to access the API
            :param entry: \w+ an integer The Entry ID
            :return data related to the ext
        """
        params = {'token': token}
        url = '/api/entries/{entry}/tags.{ext}'.format(entry=entry, ext=self.format)
        return self.query(url, params, method="post")

    def delete_entry_tag(self, token, entry, tag):
        """

            DELETE /api/entries/{entry}/tags/{tag}.{_format}

            Permanently remove one tag for an entry

            :param token: the token that identified the user to access the API
            :param entry: \w+ an integer The Entry ID
            :param tag: string The Tag
            :return data related to the ext
        """
        url = '/api/entries/{entry}/tags/{tag}.{ext}'.format(entry=entry, ext=self.format)
        params = {'token': token}
        return self.query(url, params, method="delete")

    def get_tags(self, token):
        """

            GET /api/tags.{_format}

            Retrieve all tags

            :param token: the token that identified the user to access the API
            :return data related to the ext
        """
        params = {'token': token}
        url = '/api/tags.{ext}'.format(ext=self.format)
        return self.query(url, params, method="get")

    def get_tag(self, token, tag):
        """

            GET /api/tags/{tag}.{_format}

            Retrieve a single tag

            :param token: the token that identified the user to access the API
            :param tag: string The Tag
            :return data related to the ext
        """
        url = '/api/tags/{tag}.{ext}'.format(tag=tag, ext=self.format)
        params = {'token': token}
        return self.query(url, params, method="get")


    def delete_tag(self, token, tag):
        """

            DELETE /api/tags/{tag}.{_format}

            Permanently remove one tag from every entry

            :param token: the token that identified the user to access the API
            :param tag: string The Tag
            :return data related to the ext
        """
        url = '/api/tags/{tag}.{ext}'.format(tag=tag, ext=self.format)
        params = {'token': token}
        return self.query(url, params, method="delete")
