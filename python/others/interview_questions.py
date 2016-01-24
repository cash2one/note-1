# -*- coding: utf-8 -*-

""" Python面试题 """


#################################################################
# 开胃菜
#################################################################

1、The Zen of Python是什么, 如何查看它？


2、什么是GIL？


3、平常用什么编辑器，如何调试python代码的？


4、用过哪些python包或模块，用什么管理python包的？


5、PEP8是什么?


6、os.path和sys.path的区别？


7、__init__.py 这个py文件有什么用？


#################################################################
# Python 基础篇
#################################################################

1、分别举例可变对象和不可变对象？


2、下面语句是否合法，如果合法输出什么?
(1)
>>> a, b = 1, 2
>>> a, b = b, a
>>> print a, b
(2)
>>> print 1 < 2 < 3
>>> print '0' or '1'
(3)
>>> x = y = 1
>>> z = 1
>>> print id(x) == id(y) == id(z)
>>> print x is z
(4)
>>> a, b = 1, 1.0
>>> print a == b
>>> print a is b

3、expression?A:b python如何表达?


4、switch...case.... python如何表达?


5、下列语句输出什么?

>>> a = 1
>>> b = [1]

>>> def foo(x, y):
>>>     x = 2
>>>     y + y

>>> foo(a, b)
>>> print a, b


6、如何给函数传变长参数？


7、range() 和 xrange() 的区别？


8、enumerate 的用处？


9、如何判断dict中是否存在某个key？


10、
l1 = ['key1', 'key2', 'key3', 'key4']
l2 = [1, 2, 3, 4]

如何根据l1和l2得到字典{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}


11、
>>> d = {'key': 1}
>>> l = []
>>> for x in xrange(5):
>>>     l.append(d['key']=x)
>>> print l


12、如何判断对象的类型, 比如: str、tuple、dict 或 list 等？


13、如何判断一个对象是不是可迭代对象


14、列表解析


15、list.reverse()、reversed(list)和list[::-1]的区别？


16、lambda, filter, map


17、迭代器和生成器


18、with, 如何定义支持with语句的对象？


19、异常处理, 断言？

assert isinstance('aaa', str), 'tips'

try:
    pass
except (ValueError, ):
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass


20、类的三大特性, 简单举一个多态的例子？


21、如何调用父类的方法？


22、实例方法、类方法、静态方法的区别，如何实现？


23、下面代码输出什么？

>>> class Foo(object):
>>>     a = 1

>>> obj1 = Foo()
>>> obj2 = Foo()
>>> obj1.a += 1

>>> print obj1.a, obj2.a


24、线程同步方法有哪些？


25、闭包、修饰器


26、元类，描述符


#################################################################
# Django
#################################################################

1、简述Django从Request到Response的流程？

Request -> RequestMiddleware -> URLConf -> View -> ResponseMiddleware -> Response


2、Forignkey 和 ManyToManyField
