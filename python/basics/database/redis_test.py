#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""redis-py test"""


import redis


r = redis.Redis(host='localhost', port=6379, db=0)

print r

r.set('foo', 'bar')

# r['foo'] = 'bar'

print r.get('foo')

r.delete('foo')

print r.dbsize()  # 库里有多少key, 多少条数据

# r.save()  # 强行把数据库保存到硬盘。保存时阻塞

# r.flushdb()  # 删除当前数据库的所有数据

# a = r.get('chang')  # a是None

# r.exists('chang')  # 看是否存在这个键值

# r.keys()   # 列出所有键值