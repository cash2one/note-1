#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    new some python module file
"""

__author__ = 'Pysaoke'


import os, sys


fnames = sys.argv[1:]

if not fnames:
    print "---no filename input---"
    sys.exit()

linelist = [
    "#!/usr/bin/env python",
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"doc string\"\"\"\n",
    "__author__ = \'Pysaoke\'",
    "\n\n\n\n\n\n\n\n",
    r'if __name__ == "__main__":',
    "    pass"
    ]

PY_TEMPLATE = os.linesep.join(linelist)

for fname in fnames:
    # check if the file exists already
    fname = '%s.py' % fname.split('.')[0]
    if os.path.exists(fname):
        print "WARNING:<%s> already exists" % fname
        continue

    # write lines to file
    fobj = open(fname, 'w')
    fobj.writelines(PY_TEMPLATE)
    fobj.close()
    print "OK:<%s>" % fname
