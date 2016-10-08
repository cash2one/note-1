# -*- coding: utf-8 -*-
import os
import sys


filename = "environ.txt"


while True:
    if not os.path.isfile(filename):
        break
    cmd = raw_input('ERROR: <%s> already exists' % filename)
    if cmd == 'done':
        sys.exit()
    else:
        break


with open(filename, 'wb') as f:
    env = os.environ
    keys = env.keys()
    flag = '-' * 8
    for key in keys:
        f.writelines("\n%s[%s]%s\n" % (flag, key, flag))
        lpath = env[key].split(';')
        f.writelines('%s;%s' % (x, os.linesep) for x in lpath)
