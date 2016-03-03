# -*- coding: utf-8 -*-

"""
decorator ---- 装饰器:类似面向对象中的“装饰器设计模式
"""

def tsfunc(func):
    def wrappendFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappendFunc

def now():
    print '2015-2-1'

print now.__name__  # 函数对象有一个__name__属性,可以拿到函数的名字


# 假设我们要增强now()函数的功能,比如,在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式,称之为“装饰器”（Decorator）
# 本质上,decorator就是一个返回函数的高阶函数

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2013-12-25'

now()
print now.__name__


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂.
# 比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print '2013-12-25'

now()


# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


# 针对带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


#----------------------------例子------------------------------

import time


def clock(func):
    @functools.wraps(func)  # 修改返回函数的__name__属性和被修饰的函数一样
    def wrapper(*args, **kwargs):
        start = time.time()
        c_start = time.clock()
        ret = func(*args, **kwargs)
        print 'elapsed time -> %.1fms' % ((time.time()-start)*1000)
        print 'CPU elapsed time --> %.1fms' % ((time.clock()-c_start)*1000)
        return ret
    return wrapper


@clock
def foo(a, b):
    time.sleep(0.1)
    return a+b


# def clock(ms=True):
#     if ms:
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kwargs):
#                 start = time.time()
#                 c_start = time.clock()
#                 ret = func(*args, **kwargs)
#                 print 'elapsed time -> %.1fms' % ((time.time()-start)*1000)
#                 print 'CPU elapsed time --> %.1fms' % ((time.clock()-c_start)*1000)
#                 return ret
#             return wrapper
#     else:
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*args, **kwargs):
#                 start = time.time()
#                 c_start = time.clock()
#                 ret = func(*args, **kwargs)
#                 print 'elapsed time -> %.4fs' % (time.time()-start)
#                 print 'CPU elapsed time --> %.4fs' % (time.clock()-c_start)
#                 return ret
#             return wrapper
#     return decorator


def clock(ms=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            st, c_st = time.time(), time.clock()
            ret = func(*args, **kwargs)
            print 'elapsed time: %.1fms' % ((time.time()-st)*1000) if ms else 'elapsed time: %.4fs' % (time.time()-st)
            print 'CPU time: %.1fms' % ((time.clock()-c_st)*1000) if ms else 'CPU time: %.4fs' % (time.clock()-c_st)
            return ret
        return wrapper
    return decorator


@clock(ms=True)
def foo(a, b):
    time.sleep(0.1)
    return a+b
