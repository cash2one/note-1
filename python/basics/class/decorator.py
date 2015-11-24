# -*- coding: utf-8 -*-

""" Decorator ---- 装饰器 """

from time import ctime, sleep


def tsfunc(func):
    def wrappendFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappendFunc

@tsfunc
def foo():
    print'i am foo'
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

