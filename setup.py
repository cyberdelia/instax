# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

setup(
    name='instax',
    version='0.1.6',
    description='Making celery monitoring easier.',
    author='Timothee Peignier',
    author_email='timothee.peignier@tryphon.org',
    url='https://github.com/cyberdelia/instax',
    license=license,
    py_modules=['instax'],
    install_requires=[
        "statsd>=0.5.1"
    ]
)
