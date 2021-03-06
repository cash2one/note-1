# -*- coding: utf-8 -*-

"""
例子中的select()函数通常是一个在各种文件描述符上轮询的阻塞调用
"""

import time
import gevent
from gevent import select


start = time.time()

tic = lambda: 'at %1.1f seconds' % (time.time() - start)


def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())


def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())


def gr3():
    print("Hey lets do some stuff while the Greenlets poll, %s" % tic())
    gevent.sleep(1)


gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
