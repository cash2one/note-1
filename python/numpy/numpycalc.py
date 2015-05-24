#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import random


a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a-b
print c, '\n'
print b**2, '\n'
print 10*np.sin(a), '\n'
print a<35, '\n'

#NumPy中的乘法运算符*指示按元素计算，矩阵乘法可以使用dot函数或创建矩阵对象实现
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
print A*B
print np.dot(A,B), '\n'

#操作符像+=和*=被用来更改已存在数组而不创建一个新的数组。
a = ones((2,3), dtype=int)
b = random.random((2,3))
print a *= 3
b += a
print b

#当运算的是不同类型的数组时，结果数组和更普遍和精确的已知(这种行为叫做upcast)



#指定axis参数你可以吧运算应用到数组指定的轴上
b = arange(12).reshape(3,4)
print b
print b.sum(axis=0)
print b.min(axis=1)
print b.cumsum(axis=1)

##NumPy提供常见的数学函数如sin,cos和exp。在NumPy中，这些叫作“通用函数”(ufunc)。
##在NumPy里这些函数作用按数组的元素运算，产生一个数组作为输出。
B = arange(3)
print B
print np.exp(B)
print np.sqrt(B)
C = array([2., -1., 4.])
print np.add(B, C)
##更多函数all, alltrue, any, apply along axis, argmax, argmin, argsort, average,
##bincount, ceil, clip, conj, conjugate, corrcoef, cov, cross, cumprod, cumsum,
##diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min,
##minimum, nonzero, outer, prod, re, round, sometrue, sort, std, sum, trace,
##transpose, var, vdot, vectorize, where 

##############################################################################
##索引，切片和迭代
##############################################################################
##一维数组可以被索引、切片和迭代，就像列表和其它Python序列。
a = arange(10)**3
print a
print a[2]
print a[2:5]

#from start to position 6, exclusive, set every 2nd element to -1000
print a[:6:2] = -1000 # equivalent to a[0:6:2] = -1000;
print a[ : :-1]  # reversed a

for i in a:
    print i**(1/3.)
