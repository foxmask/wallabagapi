============
Wallabag API
============

Python API for Wallabagap

Requirements :
==============
* requests == 2.5.0


Installation:
=============
to get the project, from your virtualenv, do :

.. code:: python

    git clone https://github.com/foxmask/wallabag-api/


Testing :
=========
If you plan to run python wallabag_test.py, then first of all you will need to do 

.. code:: python
    
    pip install Flask

then 

.. code:: python

    python wallabag_mock.py 

to start a Flask environment which will respond to all the request of the test you will start with python wallabag_test.py


TODO :
======

Wait the final release of http://v2.wallabag.org to be able to use the REST API (http://v2.wallabag.org/api/doc/) completly
this final release should be able to provide a token

