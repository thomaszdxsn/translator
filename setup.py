#! /usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='trans',
    version='0.1',
    py_modules=['hello'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        trans=main:cli
    ''',
)