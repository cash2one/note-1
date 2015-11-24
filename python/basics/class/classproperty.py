# -*- coding: utf-8 -*-

"""类属性和实例属性"""


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

'''
修改类属性要用类名，而不是实例名
'''

