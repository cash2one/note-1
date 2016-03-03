#!/usr/bin/env python
# -*- coding: utf-8 -*-

def define():
    a = 10
    b = 'abcdef'
    print id(a)
    print id(b)
    return a, b

x, y = define()

print
print id(x)
print id(y)
