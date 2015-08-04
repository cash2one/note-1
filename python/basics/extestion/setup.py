#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name = 'Extest',
      version = '0.0.1',
      author = 'BreatheSW',
      author_email = 'baixuexue123@gmail.com',
      url = 'http://www.baixue.com',
      download_url = '',
      description = '',
      license = 'MIT',
      ext_modules=[Extension('Extest', ['extest2.c'])],
      )
