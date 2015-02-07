# -*- coding: utf-8 -*-
__author__ = 'foxmask'
import json
from flask import Flask

"""
    The main purpose of this script is to replace v2.wallabag.org itself
    just run :
    python wallabag_mock.py &
    and then you can launch
    python wallabag_test.py

"""

app = Flask(__name__)


@app.route('/api/entries.json', methods=['GET'])
def get_entries():
    my_data = dict()
    my_data['entry'] = 'first content'
    my_data['entry'] = 'second content'
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/entries.json', methods=['POST'])
def post_entries():
    url = ''
    title = ''
    tags = []
    return json.dumps(True)


@app.route('/api/entries/<int:entry>.json', methods=['GET'])
def get_entry(entry):
    my_data = dict()
    if entry == 1:
        my_data['entry'] = 'third content'
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/entries/<int:entry>.json', methods=['PATCH'])
def patch_entries(entry, **params):
    entry = 1
    params = {'title': '',
              'archive': 0,
              'tags': [],
              'star': 0,
              'delete': 0}

    if entry == 1 and len(params) > 0:
        return json.dumps(True)
    else:
        return json.dumps(False)


@app.route('/api/entries/<int:entry>.json', methods=['DELETE'])
def delete_entries(entry):
    if entry == 1:
        return json.dumps(True)
    else:
        return json.dumps(False)


@app.route('/api/entries/<int:entry>/tags.json', methods=['GET'])
def get_entry_tags(entry):
    my_data = dict()
    if entry == 1:
        my_data = ['tag1', 'tag2', 'tag3']
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/entries/<int:entry>/tags.json', methods=['POST'])
def post_entry_tags(entry, **params):
    my_data = dict()
    if entry == 1:
        my_data = ['tag1', 'tag2', 'tag3']
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/entries/<int:entry>/tags/<tag>.json', methods=['DELETE'])
def delete_entry_tag(entry, tag):
    return json.dumps(entry, tag, encoding='utf-8')


@app.route('/api/tags.json', methods=['GET'])
def get_tags():
    my_data = ['tag1', 'tag2', 'tag3']
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/tags/<tag>.json', methods=['GET'])
def get_tag(tag):
    my_data = 'tag1'
    return json.dumps(my_data, encoding='utf-8')


@app.route('/api/tags/<tag>.json', methods=['DELETE'])
def delete_tag(tag):
    my_data = 'tag1'
    return json.dumps(my_data, encoding='utf-8')


if __name__ == '__main__':
    app.run(debug=True)

