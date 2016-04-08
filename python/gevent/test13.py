# -*- coding: utf-8 -*-

"""
gevent.queue.Queue
"""

import gevent
from gevent.queue import Queue
from gevent.queue import PriorityQueue


# tasks = Queue()


# def worker(n):
#     while not tasks.empty():
#         task = tasks.get()
#         print('Worker %s got task %s' % (n, task))
#         gevent.sleep(0)

#     print('Quitting time!')

# def boss():
#     for i in xrange(1, 25):
#         tasks.put_nowait(i)

# gevent.spawn(boss).join()

# gevent.joinall([
#     gevent.spawn(worker, 'steve'),
#     gevent.spawn(worker, 'john'),
#     gevent.spawn(worker, 'nancy'),
# ])


tasks = PriorityQueue()

tasks.put((3, '3'))
tasks.put((5, '5'))
tasks.put((1, '1'))

print tasks.get()
print tasks.get()
print tasks.get()
