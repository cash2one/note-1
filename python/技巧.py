#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''技巧'''

__author__ = 'baixue'


# 用可迭代对象创建列表
lst = ['a', 'b', 'c', 'd']
iterobj = enumerate(lst)
lista = list(iterobj)

# 用可迭代对象的前N个元素创建list
import itertools
y = list(itertools.islice(lst, N))

# 并行地循环多个可迭代对象
a = ['a1', 'a2', 'a3', 'a4', 'a5']
b = ['b1', 'b2', 'b3']
import itertools
for x, y in itertools.izip(a, b):
    print x, y

# 内建函数zip是个备选方案，缺点是它可能会损害性能
for x, y in zip(a, b):
    print x, y

# 如果迭代多个不同长度的可迭代对象，最短的可迭代对象耗尽时，zip和itertools.izip都会停止
# 在较短的可迭代对象中填充None，直到和最长的相等
for x, y in map(None, a, b):
    print x, y

# 用None之外的值填充
# 如果只有两序列用这个函数
import itertools
def par_two(a, b, padding_item=None):
    a, b = iter(a), iter(b)
    # 首先，对两者用izip处理，直达其中一个耗尽
    for x in itertools.izip(a, b):
        yield x
    # 下面两个循环最多只有一个能够执行
    # 因为此时a或b至少有一个是耗尽的
    for x in a:
        yield x, padding_item
    for x in b:
        yield padding_item, x

# 通用的，任意数目的序列
def par_loop(padding_item, *sequences):
    iterators = map(iter, sequences)
    num_remaining = len(iterators)
    result = [padding_item] * num_remaining
    while num_remaining:
        for i, it in enumerate(iterators):
            try:
                result[i] = it.next()
            except StopIteration:
                iterators[i] = itertools.repeat(padding_item)
                num_remaining -= 1
                result[i] = padding_item
        if num_remaining:
            yield tuple(result)


def smallmerge(*sequences):
    '''合并有序序列'''
    result = []
    for subseq in sequences:result.extend(subseq)
    return result


#-------------------无需过多援引 ，创建字典---------------------#
dt = dict(zip(keys, values))
dt = dict(itertools.izip(keys, values))

dt = dict(map(None, a, range(3)))
import string
count_by_letter = dict.fromkeys(string.ascii_lowercase, 0)


#-------------------字典操作技巧---------------------#
import itertools

HEADER = ('name', 'id', 'cell', 'mail')

lines = [[i for x in range(4)] for i in range(10000)]
print len(lines)

def tansform_user_data(user_data):
    '''将列表构建成和字段对应的字典'''
##    line = ['' for i in range(len(HEADER))]
##    dict_data = dict(zip(HEADER, line))
    # 字典推导式
    # dict_data = { h:'' for h in HEADER }
    dict_data = dict.fromkeys(HEADER, '')
    dict_list = []
    for data in user_data:
        dt = dict_data.copy()
        for idx, field in enumerate(HEADER):
            dt[field] = data[idx]
        dict_list.append(dt)
    return dict_list


def tansform_user_data10(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_data = dict.fromkeys(HEADER, '')
    dict_list = []
    for data in user_data:
        dt = dict_data.copy()
        for h, d in itertools.izip(HEADER, data):
            dt[h] = d
        dict_list.append(dt)
    return dict_list


def tansform_user_data2(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_list = []
    for data in user_data:
        dt = dict(zip(HEADER, data))
        dict_list.append(dt)
    return dict_list


def tansform_user_data3(lines):
    '''将列表构建成和字段对应的字典'''
    return [dict(itertools.izip(HEADER, line)) for line in lines]


def tansform_user_data4(user_data):
    '''将列表构建成和字段对应的字典'''
    dict_list = []
    for data in user_data:
        dt = dict({'id':'', 'name':''})
        for idx, field in enumerate(HEADER):
            dt[field] = data[idx]
        dict_list.append(dt)
    return dict_list
