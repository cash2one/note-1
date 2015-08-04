#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''给class动态添加属性'''

__author__ = 'baixue'


class A(object):
    a = 1
    b = 2

    def fun1(self):
        pass

    def fun2(self):
        pass

a1 = A()

a1.c = 1  # 只是增加实例的属性而不是增加类的属性

print a1.c

if hasattr(A, 'c'):  # >>> False
    print A.c

setattr( A, 'd', 1)
if hasattr(A, 'd'):  # >>> True
    print A.d

# setattr( a1.__class__, 'd', 1)

a2 = A()
print a2.d

a3 = A()
print a3.d

A.d = 2

print a2.d
print a3.d
print A.d


#---------------------------------------------------------------------------------
class C(object):
    version = 1

    def __init__(self):
        self.name = 'baixue'

hasattr(C, 'version')  # >>> True
hasattr(C, 'name')  # >>> False

c = C()
hasattr(c, 'name')  # >>> True