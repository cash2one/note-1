# -*- coding: utf-8 -*-

"""
定义一个非确定性的(non-deterministic)的task函数(给定相同输入的情况下,它的输出不保证相同).
此例中执行这个函数的副作用就是,每次task在它的执行过程中都会随机地停某些秒.
"""

import random_note
import gevent


def task(pid):
    """Some non-deterministic task"""
    gevent.sleep(random_note.randint(0, 2) * 0.001)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()


print('Asynchronous:')
asynchronous()
