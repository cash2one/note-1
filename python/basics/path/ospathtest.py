#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


curPath = os.path.dirname(__file__)
fPath = os.path.join(curPath, os.path.pardir)
print fPath

PROJECT_PATH = os.path.abspath(fPath)

print PROJECT_PATH


MEDIA_ROOT = os.path.join(PROJECT_PATH,'static')

print MEDIA_ROOT


DIRNAME = os.path.dirname(__file__)
print "dirname=%s" % DIRNAME

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
    os.path.pardir
))
print "PROJECT_ROOT=%s" % PROJECT_ROOT
