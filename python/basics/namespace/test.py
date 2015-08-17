#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''测试模块变量的作用域'''


SET = 1

print 'id:%d' % id(SET), SET

def add():
    local = SET
    local = local + 1
    print 'id:%d' % id(local), local

def add2():
    local = SET
    local = local + 1
    print 'id:%d' % id(local), local

add()
add2()

print 'id:%d' % id(SET), SET









