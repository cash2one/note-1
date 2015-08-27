#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    new a python module file
'''

__author__ = 'Pysaoke'

import os, sys


try:
    fname = sys.argv[1]
except IndexError:
    fname = raw_input("please enter the filename:")
    if not fname:sys.exit()

# check if the file exists already
fname = '%s.py' % fname
if os.path.exists(fname):
    print "ERROR:<%s> already exists" % fname
    sys.exit()

linelist = [
    '#!/usr/bin/env python',
    '# -*- coding: utf-8 -*-\n',
    '\'\'\'doc string\'\'\'\n',
    '__author__ = \'Pysaoke\'',
    '\n\n\n\n\n\n\n\n',
    r'if __name__ == "__main__":',
    '    pass'
    ]

# write lines to file
fobj = open(fname, 'w')
fobj.writelines('\n'.join(linelist))
fobj.close()
