.. image:: http://img.shields.io/badge/python-3.6-orange.svg
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

* aiohttp


Installation:
=============

to get the project, from your virtualenv, do :

.. code:: python

    git clone https://github.com/push-things/wallabag_api/


or

.. code:: python

    pip install wallabag_api



Creating a post :
=================

1) request the token, if you don't have it yet
2) create the post

.. code:: python

    #!/usr/bin/env python

    import aiohttp
    import asyncio

    from wallabag_api.wallabag import Wallabag
    # settings
    my_host = 'http://localhost:8080'


    async def main(loop):

        params = {'username': 'foxmask',
                  'password': 'mypass',
                  'client_id': 'myid',
                  'client_secret': 'mysecret',
                  'extension': 'pdf'}

        # get a new token
        token = await Wallabag.get_token(host=my_host, **params)

        # initializing
        async with aiohttp.ClientSession(loop=loop) as session:
            wall = Wallabag(host=my_host,
                            client_secret=params.get('client_secret'),
                            client_id=params.get('client_id'),
                            token=token,
                            extension=params['extension'],
                            aio_sess=session)

            url = 'https://foxmask.trigger-happy.eu'
            title = 'foxmask\'s  blog'

            await wall.post_entries(url, title, '', 0, 0)

            url = 'https://trigger-happy.eu'
            title = 'Project TrigerHappy'

            await wall.post_entries(url, title, '', 0, 0)

            # get all the articles
            my_wallabag = await wall.get_entries()

            all_article = my_wallabag['_embedded']['items']

            for article in all_article:
                print(article['id'], article['title'])

            # get the version of wallabag
            version = await wall.version
            print(f"version {version}")

            # export one article into PDF
            my_wallabag = await wall.get_entry_export(entry=1)
            with open("foobar.pdf", "wb") as f:
                f.write(my_wallabag)

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(loop))


this will give you something like this :

.. image:: https://github.com/push-things/wallabag_api/blob/master/wallabag.png


Testing :
=========

Install Wallabag V2 on your own host like explain here http://doc.wallabag.org/en/v2/user/installation.html

Then run the development version (with make run)

Then create a client API like explain here http://doc.wallabag.org/en/v2/developer/api.html

this will give you something like this

.. image:: https://github.com/push-things/wallabag_api/blob/master/wallabag_api_key.png

Then replace the client_id / client_secret / login / pass to wallabag_test.py and run

.. code:: python

    python wallabag_test.py

