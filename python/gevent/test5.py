#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
greenlet具有确定性。在相同配置相同输入的情况下，它们总是 会产生相同的输出.
下面就有例子，我们在multiprocessing的pool之间执行一系列的 任务，与在gevent的pool之间执行作比较.

即使gevent通常带有确定性，当开始与如socket或文件等外部服务交互时， 不确定性也可能溜进你的程序中。
因此尽管gevent线程是一种“确定的并发”形式， 使用它仍然可能会遇到像使用POSIX线程或进程时遇到的那些问题。
'''


import time


def echo(i):
    time.sleep(0.001)
    return i


# Non Deterministic Process Pool

from multiprocessing.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
run2 = [a for a in p.imap_unordered(echo, xrange(10))]
run3 = [a for a in p.imap_unordered(echo, xrange(10))]
run4 = [a for a in p.imap_unordered(echo, xrange(10))]

print(run1 == run2 == run3 == run4)


# Deterministic Gevent Pool

from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, xrange(10))]
run2 = [a for a in p.imap_unordered(echo, xrange(10))]
run3 = [a for a in p.imap_unordered(echo, xrange(10))]
run4 = [a for a in p.imap_unordered(echo, xrange(10))]

print(run1 == run2 == run3 == run4)
