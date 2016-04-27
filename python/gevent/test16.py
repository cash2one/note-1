# -*- coding: utf-8 -*-

"""
Queue.get()回阻塞其他的worker
"""

import gevent
from gevent.queue import Queue


tasks = Queue()


def worker_a():
    print 'worker: a'
    gevent.sleep(1)


def worker_b():
    while True:
        tasks.get(block=True)
        print 'worker: b'


worker_a = gevent.spawn(worker_a)
worker_b = gevent.spawn(worker_b)

gevent.sleep(10)

worker_a.kill()
worker_b.kill()

print 'done'
