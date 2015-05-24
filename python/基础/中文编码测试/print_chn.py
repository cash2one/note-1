#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''print 中文'''

__author__ = 'baixue'

import os

print '白雪'
print '白雪'.decode('utf-8')
print u'白雪'
print u'白雪'.encode('gbk')
print os.getcwd()

##raw_input('完成'.decode('utf-8'))
raw_input('完成:'.decode('utf-8').encode('gbk'))




if __name__ == "__main__":
    pass
