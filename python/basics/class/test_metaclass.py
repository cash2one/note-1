# -*- coding: utf-8 -*-


class BaseClass(object):
	name = 'BaseClass'

	def __init__(self):
		super(BaseClass, self).__init__()


class A(BaseClass):
	name = 'A'
	def __init__(self):
		super(A, self).__init__()


class B(BaseClass):
	name = 'B'
	def __init__(self):
		super(B, self).__init__()


a = A()
b = B()

print a.__class__
print A.__class__


print b.__class__
print B.__class__
