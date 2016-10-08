# -*- coding: utf-8 -*-
import time
import numpy as np


a = np.array([20, 30, 40, 50, 40, 50, 60, 70, 80])
b = np.arange(10)
print b

start = time.clock()

for i in range(100):
    a = np.append(a, b)
    # a = np.concatenate((a, b), axis=0)

print len(a)

stop = time.clock()

print stop - start
