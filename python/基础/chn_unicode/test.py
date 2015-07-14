#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


ROOT = os.getcwd()

print len('白雪')
print len(u'白雪')
print len(unicode('白雪', 'gbk'))

##file_path = os.path.join(ROOT, u'白雪'.encode('gbk'), u'白雪.txt'.encode('gbk'))
##print file_path
##
##file_path = os.path.join(ROOT, '白雪一'.decode('utf-8').encode('gbk'))
##print file_path
##os.mkdir(file_path)

file_path = os.path.join(ROOT, u'白雪二'.encode('gbk'))
print file_path
os.mkdir(file_path)
