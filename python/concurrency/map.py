# -*- coding: utf-8 -*-
import time
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import gevent


urls = [
    'http://www.sohu.com',
    'http://www.sina.com',
    'http://www.qq.com/',
    'http://python.jobbole.com/',
    'http://www.zhaopin.com/',
    'http://www.jd.com/',
    'http://www.zhibo8.cc/',
    'http://www.iqiyi.com/',
    'http://www.bootcss.com/',
    'http://www.redis.cn/',
    'http://cnodejs.org/',
    'http://bbs.tianya.cn/',
]

def urlopen(url):
    return urllib2.urlopen(url).info()

# single thread
st = time.time()
for url in urls:
    ret = urlopen(url)
print 'single-thread: %s' % (time.time() - st)
print
print


# multiprocessing
pool = ThreadPool(4)
st = time.time()
results = pool.map(urlopen, urls)
pool.close()
pool.join()
print 'multiprocessing.ThreadPool: %s' % (time.time() - st)
print
print


pool = ProcessPool(4)
st = time.time()
r = pool.map(urlopen, urls)
pool.close()
pool.join()
print 'multiprocessing.ProcessPool: %s' % (time.time() - st)
print
print


# futures
executor = ThreadPoolExecutor(max_workers=4)
st = time.time()
executor.map(urlopen, urls)
executor.shutdown()
print 'futures.ThreadPoolExecutor: %s' % (time.time() - st)
print
print


executor = ProcessPoolExecutor(max_workers=4)
st = time.time()
executor.map(urlopen, urls)
executor.shutdown()
print 'futures.ProcessPoolExecutor: %s' % (time.time() - st)
print
print


# gevent
from gevent import monkey; monkey.patch_socket()

st = time.time()
threads = [gevent.spawn(urlopen, i) for i in urls]
rets = gevent.joinall(threads)
print 'Gevent: %s' % (time.time() - st)
print

################################################
################################################
################################################

import itertools
import functools


def urlopen(url, param):
    return urllib2.urlopen(url)


pool = ThreadPool(4)
st = time.time()


# 方法一
# def func(args):
#     return urlopen(*args)
#
# param = 'aaaaa'
# if hasattr(param, '__iter__'):
#     reqs = itertools.izip(urls, param)
# else:
#     reqs = itertools.izip(urls, itertools.repeat(param))
#
# results = pool.map(func, reqs)


# 方法二
# func = functools.partial(urlopen, param='1111')
# results = pool.map(func, urls)


pool.close()
pool.join()

print 'ThreadPool: %s' % (time.time() - st)
print
print
