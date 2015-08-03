#!/usr/bin/python
# -*- coding: utf-8 -*-

'''class'''

__author__ = 'baixue'


'''特殊的类属性'''
class C(object):pass

C.__name__
C.__doc__
C.__bases__
C.__dict__
C.__module__
C.__class__
C.__mro__


'''内建类型没有__dict__属性'''


'''类属性，实例属性'''

class C(object):
    version = 1.2

c = C()

C.version  # >>> 1.2
'''
python首先会在c实例中搜索version，然后是C类，再就是继承树中的基类.
本例中，version再C类中被找到
'''
c.version  # >>> 1.2
C.version += 0.1
C.version  # >>> 1.2
c.version  # >>> 1.2

'''
只能使用类引用来更新类属性的值，如上例，如果用类实例c来更新version，那么会创建一个c.version的实例属性，而不会
更新类属性.
'''

'''修改类属性要用类名，而不是实例名'''



'''类，实例和其他对象的内建函数'''

issubclass()

isinstance()

hasattr()
getattr()
setattr()
delattr()

dir()

vars()


















if __name__ == "__main__":
    pass