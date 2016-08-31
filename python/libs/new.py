#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
new some python module file
author: Pysaoke
"""

import os
import sys


fnames = sys.argv[1:]

if not fnames:
    sys.exit('---no filename input---')

lines = [
    "#!/usr/bin/env python",
    "# -*- coding: utf-8 -*-\n",
    "\"\"\"doc string\"\"\"\n",
    "__author__ = \'Pysaoke\'",
    "\n\n\n\n\n\n\n\n",
    r"if __name__ == '__main__':",
    "    pass"
]

content = os.linesep.join(lines)

for fn in fnames:
    # check if the file exists already
    fn = '%s.py' % fn.split('.')[0]
    if os.path.exists(fn):
        print "WARNING:<%s> already exists" % fn
        continue
    # write lines to file
    fobj = open(fn, 'wb')
    fobj.writelines(content)
    fobj.close()
    print "OK:<%s>" % fn
