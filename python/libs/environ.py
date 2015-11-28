#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: environ.py
# Created: 17/04/2014 12:24:47
# Author: baixue
#------------------------------------------------------------------------------

import os
import sys

# filename
fname = "environ.txt"
ls = os.linesep

while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" %fname
        cmd = raw_input()
        if cmd == "done":
            sys.exit()
        else:
            break
    else:
        break

fobj = open(fname, 'w')

env = os.environ
keys = env.keys()
flag = '-' * 8
for key in keys:
    fobj.writelines("\n%s[%s]%s\n" % (flag, key, flag))
    lpath = env[key].split(';')
    fobj.writelines('%s;%s' % (x, ls) for x in lpath)

fobj.close()
