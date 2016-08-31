# -*- coding: utf-8 -*-

"""
一个更常见的应用场景, 如异步地向服务器取数据, 取数据操作的执行时间依赖于发起取数据请求时远端服务器的负载,
各个请求的执行时间会有差别.
"""

import gevent
import gevent.monkey; gevent.monkey.patch_socket()

import urllib2
import json


def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']
    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']


def synchronous():
    for i in xrange(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in xrange(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()


print('Asynchronous:')
asynchronous()
