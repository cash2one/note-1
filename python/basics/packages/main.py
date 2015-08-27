#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''包 __init__ 测试'''

__author__ = 'Pysaoke'


import conf


print conf.test1.var
print conf.test2.var

# test3没有在__init__中import, 所以会出错
# conf.test3

from conf.foo import *

print conf.foo.foo1.var
print conf.foo.foo2.var

# foo3 没有在__init__的__all__列表中, 所以import * 没有将其导入
print conf.foo.foo3.var