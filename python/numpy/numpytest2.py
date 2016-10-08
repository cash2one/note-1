# -*- coding: utf-8 -*-
import time
import numpy as np

a = np.arange(15)
print a
print u'维数(秩rank):', a.ndim

print a[:1]
print a[:-1]

# 连接两个数组
a = np.concatenate((a[:1], a[:-1]), 1)
print a
print u'维数(秩rank):', a.ndim


alst = [0]

start = time.clock()

for i in range(1000):
    alst.append(i)
    c = np.array(alst)

stop = time.clock()

print stop - start


npalst = np.array([0])

start = time.clock()

for i in range(1000):
    _ = np.concatenate((npalst, np.array([i])), 1)

stop = time.clock()

print stop - start
