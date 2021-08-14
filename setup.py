#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

import wallabagapi

setup(

    name='wallabagapi',

    version=wallabagapi.__version__,

    packages=find_packages(),

    author="폭스마스크",
    author_email="foxmask+git@pm.me",

    description="Wallabag API to add every pages you want to your Wallabag account",
    long_description=open('README.rst').read(),

    url='https://gitlab.com/foxmask/wallabagapi',

    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Intended Audience :: Developers"
        "License :: Public Domain"
        "Operating System :: OS Independent"
        "Programming Language :: Python"
        "Programming Language :: Python :: 3.8"
        "Topic :: Internet"
        "Topic :: Communications"
    ],

    install_requires=[
        'httpx>=0.18.2'
    ],

    license="WTFPL",

)
