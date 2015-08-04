#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: ooptest.py
# Created: 20/01/2014 11:41:39
# Author: baixue
# Purpose:多态测试
#------------------------------------------------------------------------------

class base(object):
    def __init__(self):
        super(base, self).__init__()

    def show(self):
        print 'base'

class A(base):
    def show(self):
        print 'a'

class B(base):
    def show(self):
        print 'b'

class C(base):
    def show(self):
        print 'c'


if __name__ == "__main__":
    mix = base(), A(), B(), C()
    for item in mix:
        item.show()
