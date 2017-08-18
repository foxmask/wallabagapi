.. image:: http://img.shields.io/badge/python-3.6-orange.svg
    :target: https://pypi.python.org/pypi/django-th/
    :alt: Python version supported


.. image:: http://img.shields.io/badge/python-3.5-orange.svg
    :target: https://pypi.python.org/pypi/django-th/
    :alt: Python version supported


.. image:: http://img.shields.io/badge/license-BSD-blue.svg
    :target: https://pypi.python.org/pypi/django-th/
    :alt: License


============
Wallabag API
============

Python API for Wallabag v2.2.3

Requirements :
==============

* requests  2.13.0


Installation:
=============

to get the project, from your virtualenv, do :

.. code:: python

    git clone https://github.com/foxmask/wallabag-api/


or

.. code:: python

    pip install wallabag_api



Creating a post :
=================

1) request the token, if you don't have it yet
2) create the post

.. code:: python

    from wallabag_api.wallabag import Wallabag
    # settings
    params = {'username': 'foxmask',
              'password': 'mypass',
              'client_id': 'myid',
              'client_secret': 'mysecret'}
    my_host = 'http://localhost:8080'
    # get token
    token = Wallabag.get_token(host=my_host, **params)

    # create a post
    wall = Wallabag(host=my_host,
                    client_secret='mysecret',
                    client_id='myid',
                    token=token)

    my_url = 'https://blog.trigger-happy.eu'
    my_title = 'Trigger Happy blog'
    my_tags = ['python', 'wallabag']

    wall.post_entries(url=my_url, title=my_title, tags=my_tags)


this will give you something like this :

.. image:: https://github.com/foxmask/wallabag_api/blob/master/wallabag.png


3) get all the entries

.. code:: python

    # get all the entries
    wall = wall.get_entries()

    all_article = wall['_embedded']['items']

    for article in all_article:
        print(article['title'])
        print(article['content'])
        print("******")

4) version of wallabag

.. code:: python

    # get the version of your wallabag instance
    print("version {}".format(wall.version))

5) to get the article in PDF

.. code:: python

    # to get the article in PDF for example,
    wall = Wallabag(host=my_host,
                    client_secret='mysecret',
                    client_id='myid',
                    token=token,
                    extension='pdf')
    article = wall.get_entry_export(entry=1)
    with open("my_file.pdf", "wb") as f:
        f.write(article)


Testing :
=========

Install Wallabag V2 on your own host like explain here http://doc.wallabag.org/en/v2/user/installation.html

Then run the development version (with make run)

Then create a client API like explain here http://doc.wallabag.org/en/v2/developer/api.html

this will give you somthing like this

.. image:: https://github.com/foxmask/wallabag_api/blob/master/wallabag_api_key.png

Then replace the client_id / client_secret / login / pass to wallabag_test.py and run

.. code:: python

    python wallabag_test.py

