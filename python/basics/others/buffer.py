#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: buffer.py
# Created: 23/12/2013 15:53:58
# Author: baixue
# Purpose:
#------------------------------------------------------------------------------
##Type code     C Type          Python Type     Minimum size in bytes 
##'c'           char            character           1 
##'b'           signed          char int            1 
##'B'           unsigned        char int            1 
##'u'           Py_UNICODE      Unicode character   2 (see note)
##'h'           signed short    int                 2 
##'H'           unsigned short  int                 2 
##'i'           signed int      int                 2 
##'I'           unsigned int    long                2 
##'l'           signed long     int                 4 
##'L'           unsigned long   long                4 
##'f'           float           float               4 
##'d'           double          float               8
#------------------------------------------------------------------------------
from array import array

class Buffer(object):
    def __init__(self, atype, size):
        self.buf = array(atype, [])
        self.size = size

    def size(self):
        return len(self.buf)

    def append(self, item):
        if len(self.buf) >= self.size:
            del self.buf[0]
        self.buf.append(item)

    def preview(self):
        return self.buf.tolist()

    def flush(self):
        self.buf = array(atype, [])

    def mean(self):
        return sum(self.buf)//len(self.buf)

    def asum(self):
        return sum(self.buf)


if __name__ == "__main__":
    pass
