# -*- coding: utf-8 -*-
__author__ = 'foxmask'
import json
from flask import Flask, request

"""
    The main purpose of this script is to replace v2.wallabag.org itself
    just run :
    python wallabag_mock.py &
    and then you can launch
    python wallabag_test.py

"""

app = Flask(__name__)

@app.route('/api/u/<user>/entries.json', methods=['GET'])
def get(user):
    my_data = dict()
    if user == 'foxmask':
        my_data['entry'] = 'first content'
        my_data['entry'] = 'second content'
    return json.dumps(my_data,encoding='utf-8')

@app.route('/api/u/<user>/entries.json', methods=['GET'])
def get_entries(user):
    my_data = dict()
    if user == 'foxmask':
        my_data['entry'] = 'first content'
        my_data['entry'] = 'second content'
    return json.dumps(my_data,encoding='utf-8')

@app.route('/api/u/<user>/entry/<int:entry>', methods=['GET'])
def get_entry(user, entry):
    my_data = dict()
    if user == 'foxmask' and entry == 1:
        my_data['entry'] = 'third content'
    return json.dumps(my_data,encoding='utf-8')

@app.route('/api/u/<user>/entries.json', methods=['POST'])
def post_entries(user):
    if user == 'foxmask':
        return json.dumps(True)
    else:
        return json.dumps(False)

@app.route('/api/u/<user>/entries.json', methods=['PATCH'])
def patch_entries(user):
    if user == 'foxmask':
        return json.dumps(True)
    else:
        return json.dumps(False)

@app.route('/api/u/<user>/entry/<int:entry>', methods=['DELETE'])
def delete_entry(user, entry):
    if user == 'foxmask' and entry == 1:
        return json.dumps(True)
    else:
        return json.dumps(False)

if __name__ == '__main__':
    app.run(debug=True)