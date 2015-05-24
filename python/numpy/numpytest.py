#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------

import numpy as np

a = np.arange(15)
print a
print u'维数(秩rank):', a.ndim
a = np.arange(10, 30, 5)
b = np.arange(0, 2, 0.3)
print a
print b, '\n'
##当arange使用浮点数参数时，由于有限的浮点数精度,
##通常无法预测获得的元素个数.
##因此,最好使用函数linspace去接收我们想要的元素个数来代替用range来指定步长.

a = np.arange(15)
b = a.reshape(3, 5)
print b
print u'每个轴的元素个数:', b.shape
print u'维数(秩rank):', b.ndim
print u'类型:', b.dtype.name
print u'元素尺寸:', b.itemsize
print u'元素个数:', b.size
print u'类型:', type(b), '\n'

#初始化数组
c = np.array([6, 7, 8])
print c
print type(c), '\n'

#初始化时指定类型
d = np.array([6, 7, 8], dtype=float)
print d, '\n'

#初始化一个全是0的数组
arr = np.zeros((3, 4))
print arr
#全是1
arr = np.ones((2,3,4), dtype=int)
print arr
#随机数
arr = np.empty((2, 3))
print arr


