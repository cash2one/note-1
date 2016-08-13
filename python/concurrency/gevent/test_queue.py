# -*- coding: utf-8 -*-

"""
优先级队列测试
"""

from gevent.queue import PriorityQueue


tasks = PriorityQueue()

tasks.put((3, '3'))
tasks.put((5, '5'))
tasks.put((1, '1'))

print tasks.get()
print tasks.get()
print tasks.get()
