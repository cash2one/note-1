# -*- coding: utf-8 -*-
import os
import sys


filename = "environ.txt"
sep = os.linesep

while True:
    if not os.path.exists(filename):
        break
    cmd = raw_input('ERROR: <%s> already exists' % filename)
    if cmd == 'done':
        sys.exit()
    else:
        break

fobj = open(filename, 'wb')

env = os.environ
keys = env.keys()
flag = '-' * 8
for key in keys:
    fobj.writelines("\n%s[%s]%s\n" % (flag, key, flag))
    lpath = env[key].split(';')
    fobj.writelines('%s;%s' % (x, sep) for x in lpath)

fobj.close()
