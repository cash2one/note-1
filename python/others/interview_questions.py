# -*- coding: utf-8 -*-

""" Python面试题 """


1、什么是GIL？


2、平常用什么编辑器，如何调试python代码的？


3、用过哪些python包或模块，用什么管理python包的？


4、os.path和sys.path的区别？


5、__init__.py 这个文件有什么用？


#################################################################
# Python 基础篇
#################################################################

1、分别举例可变对象和不可变对象？


2、下面语句是否合法，如果合法输出什么?
(1)
>>> print 1 < 2 < 3
>>> print '0' or '1'
(2)
>>> x = y = 1
>>> z = 1
>>> print id(x) == id(y) == id(z)
>>> print x is z
(3)
>>> if 2>1:
>>>     print 'a'
>>> elif 3>1:
>>>     print 'b'
>>> elif 4>1:
>>>     print 'c'
>>> else:
>>>     print 'd'
(4)
>>> a = 1

>>> def foo(a):
>>>     a = 2

>>> foo(a)
>>> print a

3、expression?A:b python如何表达?


4、如何给函数传变长参数？


5、range() 和 xrange() 的区别？


6、enumerate 的用处？


7、
l1 = [1, 3, 5, 6, 8, 9]
l2 = [2, 0, 3, 5, 11, 10, 12]
如何取得l1和l2的重复元素


8、如何判断dict中是否存在某个key？


9、
l1 = ['key1', 'key2', 'key3', 'key4']
l2 = [1, 2, 3, 4]
如何根据l1和l2得到字典{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}


10、如何判断对象的类型, 比如: str、tuple、dict 或 list 等？


11、如何判断一个对象是不是可迭代对象？


12、用列表推导的方式提取range(1, 100)中的偶数？


13、list.reverse()、reversed(list)和list[::-1]的区别？


14、lambda, filter, map


15、迭代器和生成器


16、with, 如何定义支持with语句的对象？


17、异常处理, 断言？

assert True, 'tips'

try:
    pass
except (ValueError, IOError):
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass


18、类的三大特性, 简单举一个多态的例子？


19、如何调用父类的方法？


20、实例方法、类方法、静态方法的区别，如何定义？


21、下面代码输出什么？

>>> class Foo(object):
>>>     a = 1

>>> obj1 = Foo()
>>> obj2 = Foo()
>>> obj1.a += 1

>>> print obj1.a, obj2.a


22、python中线程同步方法有哪些？


23、闭包、修饰器


24、元类，描述符


#################################################################
# Django
#################################################################

1、简述Django从Request到Response的流程？
