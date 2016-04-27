# -*- coding: utf-8 -*-
import gevent
from gevent.queue import Queue


tasks = Queue()


def foo():
    for i in xrange(1, 14):
        tasks.put_nowait(i)

gevent.spawn(foo).join()


def worker(name):
    while True:
        if not tasks.empty():
            print name , ' -- ', tasks.get()
        gevent.sleep(1)


worker_a = gevent.spawn(worker, 'worker-A')
worker_b = gevent.spawn(worker, 'worker-B')
worker_c = gevent.spawn(worker, 'worker-C')


while True:
    if tasks.empty():
        worker_a.kill()
        worker_b.kill()
        worker_c.kill()
        break
    gevent.sleep(1)

print 'done'
