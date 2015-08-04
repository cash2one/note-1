#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Doc String'''

import os, sys


def getfile(dirs, ext=None):
    '''获取给目录内的所有文件(不包括子目录里的文件), 可以指定文件扩展名来获取指定类型的文件'''
    if not os.path.isdir(dirs):
        return
    files =  os.listdir(dirs)
    files =  filter(lambda x:os.path.isfile(os.path.join(dirs, x)), files)
    if ext:files = filter(lambda x:os.path.splitext(x)[1]==ext, files)
    return files


if __name__ == "__main__":
    dirs = '/home/baixue/deploy/CRM/src/crm'
    print getfile(dirs, ext='.py')
