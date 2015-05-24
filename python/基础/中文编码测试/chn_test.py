#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''中文编码测试'''

__author__ = 'baixue'


import os

ROOT = os.getcwd()
file_path = os.path.join(ROOT, u'白雪'.encode('gbk'), u'白雪.txt'.encode('gbk'))

with open(file_path, 'r') as fobj:
    for eachline in fobj:
        print eachline


if __name__ == "__main__":
    pass
