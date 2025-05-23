#!/usr/bin/env python
from setuptools import setup
import codecs
import os
import re
__version__ = '0.7.6'

with codecs.open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'binance',
            '__init__.py'
        ), 'r', 'latin1') as fp:
    try:
        version = __version__ # re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='python-binance',
    version=__version__,
    packages=['binance'],
    description='Binance REST API python implementation',
    url='https://github.com/sammchardy/python-binance',
    author='Sam McHardy',
    license='MIT',
    author_email='',
    install_requires=[
        'requests', 'six', 'Twisted', 'pyOpenSSL', 'autobahn', 'service-identity', 'dateparser', 'urllib3', 'chardet', 'certifi',
        'cryptography', 'aiohttp'
    ],

    keywords='binance exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
