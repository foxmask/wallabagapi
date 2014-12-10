# -*- coding: utf-8 -*-
__author__ = 'foxmask'

import requests
import logging

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

    def __init__(self, host='http://v2.wallabag.org', api_key='', user_agent="WallabagPython"):
        """
            init variable
            :param host: string url to the official API Wallabagap
            :param api_key: string of the key provided by Wallabagap
            :param user_agent
        """
        self.host = host
        self.api_key = api_key
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
        #params = params
        params['key'] = self.api_key
        if method == 'get':
            r = requests.get(self.get_host() + url, params=params)
        elif method == 'post':
            r = requests.post(self.get_host() + url, params=params)
        elif method == 'patch':
            r = requests.patch(self.get_host() + url, params=params)
        elif method == 'delete':
            r = requests.delete(self.get_host() + url, params=params)
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
                logging.error("Wallabag: %s" % \
                              json_data['errors'][error]['content'])
        return json_data

    def get(self, token, user):
        """
            List unread entries for the given user
            :param token: the token that identified the user to access the API
            :param user: the current user
            :return json data
        """
        return self.get_entries(token, user)

    def get_entries(self, token, user):
        """
            List unread entries for the given user
            :param token: the token that identified the user to access the API
            :param user: the current user
            :return json data
        """
        return self.query('/api/u/{user}/entries.json'.format(user=user), {'token': token}, method="get")

    def get_entry(self, token, user, entry):
        """
            Fetch an entry, regardless the status flags
            :param user: entry of that user
            :param entry: the entry
            :return json data
        """
        return self.query('/api/u/{user}/entry/{entry}'.format(user=user, entry=entry),
                          {'token': token}, method="get")

    def post_entries(self, token, user, url=[], tags=[]):
        """
            Save a new entry for the given user
            :param user: entry of that user
            :param url: the url of the note to store
            :param tags: the tags of the note to store if provided
            :return json data
        """
        params = {'token': token, 'url': url}
        if len(tags) > 0:
            params = {'token': token, 'url': url, 'tags': tags}
        return self.query('/api/u/{user}/entries.json'.format(user=user), params, method="post")

    def patch_entries(self, token, user, entry=[]):
        """
            Change several properties of an entry. I.E tags, archived, starred and deleted status
            :param user: entry of that user
            :param entry: the entry to 'patch'
            :return json data
        """
        params = {'token': token, 'entry': entry}
        return self.query('/api/u/{user}/entries.json'.format(user=user), params, method="patch")

    def delete_entry(self, token, user, entry):
        """
            Delete an entry
            :param user: entry of that user
            :param entry: the entry to 'delete'
            :return json data
        """
        return self.query('/api/u/{user}/entry/{entry}'.format(user=user, entry=entry), {'token': token}, method="delete")
