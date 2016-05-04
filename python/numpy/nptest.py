# -*- coding: utf-8 -*-
import numpy as np

# *************************************************************************
# 属性
# *************************************************************************

ndarray = np.arange(0, 10)

#数组的维数（即数组轴的个数）, 等于秩
ndarray.ndim

#数组的维度。为一个表示数组在每个维度上大小的整数元组
ndarray.shape

#数组元素的总个数
ndarray.size

#数组中元素类型的对象
ndarray.dtype

#itemsize--查看数组中元素占用的字节数目
ndarray.itemsize

#包含实际数组元素的缓冲区(由于一般通过数组的索引获取元素，所以通常不需要使用这个属性)
ndarray.data

#flags属性描述了数据存储区域的一些属性
ndarray.flags


# *************************************************************************
# 创建数组(Array Creation)
# *************************************************************************

ndarray = np.arange(0, 10)

ndarray = np.array([20, 30, 40, 50])

ndarray = np.array([[1, 2], [3, 4]])

ndarray = ones((2, 3), dtype=int)

ndarray = zeros(5, dtype=float)

ndarray = np.empty((2, 3))


# *************************************************************************
# 数组操作
# *************************************************************************

# vstack 和 hstack  # 合并数组
np.concatenate()  # 连接数组
np.insert()  # 插入
np.delete()  # 删除
np.vsplit()  # 拆分数组
np.transpose  # 数组转置
np.append(array, element)
np.max()
np.min()
np.mean()
np.sin()
np.add()
np.reshape()
