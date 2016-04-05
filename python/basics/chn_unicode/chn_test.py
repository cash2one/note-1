#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""中文编码测试"""

import os


ROOT = os.getcwd()
path = os.path.join(ROOT, u'白雪'.encode('gbk'), u'白雪.txt'.encode('gbk'))

with open(path, 'r') as fobj:
    for line in fobj:
        print line
