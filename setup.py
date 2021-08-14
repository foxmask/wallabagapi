#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

import wallabagapi

version = wallabagapi.__version__

setup(

    name='wallabagapi',

    version=version,

    packages=find_packages(),

    author="폭스마스크",
    author_email="foxmask+git@pm.me",

    description="Wallabag API to add every pages you want to your Wallabag account",
    long_description=open('README.rst').read(),

    url='https://gitlab.com/foxmask/wallabag_api',
    download_url='https://gitlab.com/foxmask/wallabag_api/-/archive/' + version + 'wallabagapi-' + version + '.tar.gz',

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet",
        "Topic :: Communications"
    ],

    install_requires=[
        'httpx>=0.18.2'
    ],

    license="WTFPL",

)
