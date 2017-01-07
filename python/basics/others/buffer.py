#!/usr/bin/env python
# -*- coding: utf-8 -*-

# **********************************************************************
# File: buffer.py
# Created: 23/12/2013 15:53:58
# Author: baixue
# Description:
# **********************************************************************
# Type code     C Type          Python Type     Minimum size in bytes 
# 'c'           char            character           1 
# 'b'           signed          char int            1 
# 'B'           unsigned        char int            1 
# 'u'           Py_UNICODE      Unicode character   2 (see note)
# 'h'           signed short    int                 2 
# 'H'           unsigned short  int                 2 
# 'i'           signed int      int                 2 
# 'I'           unsigned int    long                2 
# 'l'           signed long     int                 4 
# 'L'           unsigned long   long                4 
# 'f'           float           float               4 
# 'd'           double          float               8
# **********************************************************************
from __future__ import division
from array import array


class Buffer(object):
    def __init__(self, size, atype='f'):
        self.atype = atype
        self.size = size
        self.items = array(atype, [])

    def size(self):
        return len(self.items)

    def append(self, item):
        if len(self.items) >= self.size:
            del self.items[0]
        self.items.append(item)

    def pre_items(self, x):
        return self.items[0:x].tolist()

    def preview(self):
        return self.items.tolist()

    def flush(self):
        self.items = array(self.atype, [])

    def mean(self):
        return sum(self.items) / len(self.items)

    def sum(self):
        return sum(self.items)


if __name__ == "__main__":
    import time
    buf = Buffer(10)
    for i in xrange(50):
        buf.append(i)
        print buf.preview()
        print buf.pre_items(5)
        time.sleep(1)
