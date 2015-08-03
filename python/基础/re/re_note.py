#!/usr/bin/python
# -*- coding: utf-8 -*-

'''re note'''

__author__ = 'baixue'


import re


m = re.match('foo', 'foo')
if m is not None:
    print type(m)
    m.group()


m = re.match('foo', 'food on tables')
m.group()


# search()和match()区别
m = re.match('foo', 'seafood')
if m is not None:m.group()

# match()匹配不成功，search()匹配成功
m = re.search('foo', 'seafood')
if m is not None:m.group()


# 匹配子组
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
m.group()  # 'abc-123'
m.group(1)  # 'abc'
m.group(2)  # '123'
# groups() 获取所有匹配的子组
m.groups()  # ('abc', '123')


#
m = re.search('^The', 'The end.')
if m is not None:m.group()

m = re.search('^The', 'end. The')


# \b 边界
m = re.search('\bthe', 'bite the dog')
if m is not None:m.group()  # >>> 'the'

m = re.search('\bthe', 'bitethe dog')
if m is not None:m.group()  # >>> None

m = re.search('\Bthe', 'bitethe dog')
if m is not None:m.group()  # >>> 'the'


# sub()和subn()
re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
# >>> 'attn:Mr. Smith\n\nDear Mr. Smith,\n'

re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
# >>> ('attn:Mr. Smith\n\nDear Mr. Smith,\n', 2)


# re.split()










if __name__ == "__main__":
    pass