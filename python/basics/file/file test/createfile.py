# -*- coding: utf-8 -*-
import os
import sys


print 'Input FileName Please', r'\n'

filename = raw_input()

while True:
    if os.path.exists(filename):
        print "ERROR: '%s' already exists" % filename
        cmd = raw_input()
        if cmd == "done":
            sys.exit()
        else:
            break
    else:
        break

# get file content (text) lines
_all = []
print "\nEnter lines('.' by itself to quit).\n"


# loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        _all.append(entry)

# write lines to file with proper line-ending
fd = open(filename, 'w')
fd.writelines('%s%s' % (x, os.linesep) for x in _all)
fd.close()
print 'DONE!'
