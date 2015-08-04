#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'baixue'


import sys, os

print __name__
print __file__
print __doc__
#---------------------------------------------------------------

#获取当前目录
curdir =  os.getcwd()
print curdir

#获取父目录
pardir = os.path.split(curdir)[0]
print pardir

#向python搜索列表中添加目录
sys.path.append(pardir)
import buffer

#-----------------------------------------------------------------

os.path.curdir = os.getcwd()
print os.path.curdir #当前目录
print os.path.altsep #根目录
print os.path.pardir #父目录
print
print os.path.abspath("d:\\new\\test.txt") #绝对路径
print
print os.path.join("d:\\new\\", 'baixue.txt') #连接路径
print os.path.basename("d:\\new\\test.txt") #文件名
print os.path.dirname("d:\\new\\test.txt") #文件目录
print
print os.path.exists("d:\\new\\test.txt") #验证路径是否存在
print os.path.exists(os.path.join(os.getcwd(), os.path.basename(__file__)))
print
print os.path.isfile("d:\\new\\hello.txt")
print os.path.isdir(os.getcwd())









