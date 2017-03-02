# -*- coding: utf-8 -*-

""" toolkit
@author: Pysaoke
Created on 15-11-24
"""

import os
import itertools
import urllib
import urlparse
import datetime


def basename(path):
    """获取一个文件的名字,不包括扩展名"""
    return os.path.splitext(os.path.basename(path))[0]


def getfile(dir, ext=None):
    """ 获取给定目录内的所有文件(不包括子目录里的文件),可以指定文件扩展名来获取指定类型的文件
    :param dir: 目录绝对路径
    :param ext: 扩展名
    :return: list 文件列表
    """
    if not os.path.isdir(dir):
        return
    files = filter(lambda x: os.path.isfile(os.path.join(dir, x)), os.listdir(dir))
    if ext:
        files = filter(lambda x: os.path.splitext(x)[1]==ext, files)
    return files


def listget(lst, idx, default=None):
    """若列表中某索引存在则返回之"""
    if -len(lst) <= idx < len(lst):
        return lst[idx]
    else:
        return default


def list_get(lst, idx, default=None):
    """如果传递的索引绝大多数都是有效索引,那么用这个函数"""
    try:
        return lst(idx)
    except IndexError:
        return default


def par_two(a, b, padding_item=None):
    """并行地循环两个可迭代对象,短的用padding_item补充"""
    a, b = iter(a), iter(b)
    # 首先,对两者用izip处理,直达其中一个耗尽
    for x in itertools.izip(a, b):
        yield x
    # 下面两个循环最多只有一个能够执行,因为此时a或b至少有一个是耗尽的
    for x in a:
        yield x, padding_item
    for x in b:
        yield padding_item, x


def par_loop(padding_item, *sequences):
    """并行地循环多个可迭代对象,短的用padding_item补充"""
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
    """合并有序序列"""
    result = []
    for subseq in sequences:
        result.extend(subseq)
    return result


# 获取字典的子集
def sub_dict_select(x_dict, keys):
    return dict([(k, x_dict[k]) for k in keys if k in x_dict])


# 获取字典的子集,有默认值
def sub_dict(x_dict, keys, default=None):
    return dict([(k, x_dict.get(k, default)) for k in keys])


def last_month(multiple=1):
    """上几个月的日期"""
    today = datetime.date.today()
    year, month = divmod(multiple, 12)
    offset = today.month - month
    if offset <= 0:
        return datetime.date(today.year-year-1, 12+offset, 1).strftime('%Y.%m')
    else:
        return datetime.date(today.year-year, offset, 1).strftime('%Y.%m')


def gen_date():
    return map(last_month, range(6))


def get_qs(url):
    """parse a URL query string"""
    query = urlparse.urlparse(url).query
    return dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])


def add_qs(url, **kwargs):
    """ 添加url参数
    :param params 用这个关键字参数输入字典类型
    """
    kwargs.update(kwargs.pop('params', ''))
    qs = urllib.urlencode(kwargs)
    if not qs:
        return url
    if not get_qs(url):
        return url+'?'+qs
    else:
        return url+'&'+qs


def group_generator(data, chunksize):
    """将迭代器分组返回"""
    chunk = []
    for d in data:
        chunk.append(d)
        if len(chunk) == chunksize:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def read_in_chunks(fd, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = fd.read(chunk_size)
        if not data:
            break
        yield data


def group_generator1(fd, chunk_size=1000):
    chunk = [x for x in itertools.islice(fd, chunk_size)]
    if chunk:
        yield chunk


if __name__ == '__main__':
    url = 'crm.100credit.cn?a=1'
    print add_qs(url, params={'a': 1, 'b': 3}, c='c', d='ddd')
