#!/usr/bin/env python
# coding=UTF-8
from setuptools import setup, find_packages


setup(keywords=['smok', 'api', 'rest', 'client', 'smok.co'],
      packages=find_packages(include=['smok', 'smok.*']),
      long_description=u'''The definitive client for all SMOK matters''',
      install_requires=['requests'],
      # per coverage version for codeclimate-reporter
      tests_require=["nose", 'coverage>=4.0,<4.4'],
      test_suite='nose.collector'
     )
