# -*- coding: utf-8 -*-

""" 面试题 """


#################################################################
# 开胃菜
#################################################################

1、The Zen of Python是什么, 如何查看它？

Python之禅, import this


2、什么是GIL？

GIL(Global Interpreter Lock)全局解释器锁
每一个interpreter进程,只能同时仅有一个线程来执行, 获得相关的锁, 存取相关的资源.  
那么很容易就会发现,如果一个interpreter进程只能有一个线程来执行,   
多线程的并发则成为不可能


#################################################################
# Python 基础篇
#################################################################

3、range()和xrange()的区别？


5、zip

有两个列表 
l1 = ['key1', 'key2', 'key3', 'key4']
l2 = [1, 2, 3, 4]

怎么得到字典{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

dict(zip(l1, l2))


6、lambda


6、filter, map


7、list.reverse()、reversed(list)和list[::-1]的区别？

l =  range(10)
l.reverse()  # l 被翻转
reversed(l)  # 返回l的反向迭代器
l[::-1]      # 返回翻转的l的新对象


8、with的使用, 如何定义支持with语句的对象？


#################################################################
# 标准库
#################################################################

1、os


2、random

random.random()
random.randint(1,11)
random.choice(range(11))
random.shuffle()


3、itertools


4、collections


#################################################################
# Django
#################################################################

1、简述Django从Request到Response的流程？

Request -> RequestMiddleware -> URLConf -> View -> ResponseMiddleware -> Response

