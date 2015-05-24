#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''create a new python module file'''

__author__ = "baixue"

import os
import sys


fname = raw_input("file name:")

if fname=='':
    sys.exit()

# check if the file exists already
fname = '%s.py' % fname
if os.path.exists(fname):
    raw_input("ERROR:'%s' already exists" % fname)
    sys.exit()

linelist = [
    '#!/usr/bin/env python',
    '# -*- coding: utf-8 -*-\n',
    '\'\'\'Doc String\'\'\'\n',
    '__author__ = \'baixue\'',
    '\n\n\n\n\n\n\n\n',
    r'if __name__ == "__main__":',
    '    pass'
    ]

# write lines to file
fobj = file(fname, 'w')
fobj.writelines('\n'.join(linelist))
fobj.close()
