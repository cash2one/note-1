
'makeTextFile.py--create text file'


import os
import sys

ls = os.linesep

print 'Input FileName Please', r'\n'

fname = raw_input()

# get filename
while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
        cmd = raw_input()
        if cmd == "done":
            sys.exit()
        else:
            break
    else:
        break

# get file content (text) lines
all = []
print "\nEnter lines('.' by itself to quit).\n"

#loop until user terminates input
while True:
    entry = raw_input('>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines('%s%s' % (x, ls) for x in all)
fobj.close()
print 'DONE!'
