# -*- coding: utf-8 -*-

""" Python面试题 """


#################################################################
# 开胃菜
#################################################################

1、The Zen of Python是什么, 如何查看它？


2、什么是GIL？


3、平常用什么编辑器，是如何调试python代码的？


4、用过哪些python包或模块，用什么管理python包的？


5、如何查看一个模块或类的帮助信息?


6、PEP8是什么?


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
>>> x = y = z = 1
>>> print id(x) == id(y) == id(z)
>>> print x is y
(3)
>>> a, b = 1, 1.0
>>> print a == b

3、expression?A:b python如何表达?


4、switch...case.... python如何表达?


5、下列语句输出什么?

>>> a = 1
>>> b = [2]
>>> c = ['test']

>>> def foo(x, y, z):
>>>     x = 2
>>>     y = 5
>>>     z[0] = 3

>>> foo(a, b, c)
>>> print a, b, c


6、如何传递变长参数？


7、range()和xrange()的区别？


8、enumerate 的用处？


9、python字典的key有什么限制，python哪些类型不可以做字典的键？


10、有两个列表
l1 = ['key1', 'key2', 'key3', 'key4']
l2 = [1, 2, 3, 4]

如何得到字典{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}


11、如何判断对象的类型是不是 str、tuple、dict 或是 list 等？


12、如何判断一个对象是不是可迭代对象


13、列表解析


14、迭代器和生成器


16、lambda, filter, map, yield


17、如何提取range(100)中的奇数


18、list.reverse()、reversed(list)和list[::-1]的区别？

l =  range(10)
l.reverse()  # l 被翻转
reversed(l)  # 返回l的反向迭代器
l[::-1]      # 返回翻转的l的新对象


19、with, 如何定义支持with语句的对象？


20、异常处理, 断言？

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


21、类的三大特性, 简单举一个多态的例子？


22、实例方法、类方法、静态方法的区别，如何实现？


23、如何调用父类的方法？


24、静态变量、实例变量

class Foo(object):
    a = 1

obj = Foo()
obj.a += 2
print obj.a


class Person:
    name='aaa'

p1=Person()
p2=Person()
p1.name='bbb'
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa


class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print p1.name  # [1]
print p2.name  # [1]
print Person.name  # [1]


25、多线程、多进程、协程，线程同步方法有哪些？


26、闭包、修饰器


27、元类，描述符


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


2、Forignkey 和 ManyToManyField
