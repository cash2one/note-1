#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''toolkits'''

__author__ = 'baixue'


import os, sys
import itertools


def get_basename(path):
    '''获取一个文件的名字，不包括扩展名'''
    return os.path.splitext(os.path.basename(path))[0]


def getfile(dirs, ext=None):
    '''获取给目录内的所有文件(不包括子目录里的文件), 可以指定文件扩展名来获取指定类型的文件'''
    if not os.path.isdir(dirs):
        return
    files =  os.listdir(dirs)
    files =  filter(lambda x:os.path.isfile(os.path.join(dirs, x)), files)
    if ext:files = filter(lambda x:os.path.splitext(x)[1]==ext, files)
    return files


def listget(lst, idx, default=None):
    '''若列表中某索引存在则返回之'''
    if -len(lst) <= idx < len(lst):return lst[idx]
    else:return default


def list_get(lst, idx, default=None):
    '如果传递的索引绝大多数都是有效索引，那么用这个函数'
    try:return lst(idx)
    except IndexError:return default


def par_two(a, b, padding_item=None):
    '''并行地循环两个可迭代对象, 短的用padding_item补充'''
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


def par_loop(padding_item, *sequences):
    '''并行地循环多个可迭代对象, 短的用padding_item补充'''
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







