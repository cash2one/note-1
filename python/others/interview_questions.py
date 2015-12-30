# -*- coding: utf-8 -*-

""" 面试题 """


#################################################################
# 开胃菜
#################################################################

1、The Zen of Python是什么, 如何查看它？

Python之禅, import this


2、什么是GIL？

GIL(Global Interpreter Lock)全局解释器锁
Python为了保证线程安全而采取的独立线程运行的限制
每一个interpreter进程,只能同时仅有一个线程来执行, 获得相关的锁, 存取相关的资源.
那么很容易就会发现,如果一个interpreter进程只能有一个线程来执行, 多线程的并发则成为不可能


3、平常用什么编辑器，如何调试代码？


4、用过哪些python包或模块，用什么管理python的包的？


5、如何查看一个模块或类的帮助信息


6、http、https和tcp/ip


#################################################################
# Python 基础篇
#################################################################

1、分别举例可变对象和不可变对象？


2、变量

a, b = b, a  # 交换两个变量的值

x = y = z = 1   # id(x) == id(y) == id(z)


3、expression?A:b python如何表达


4、switch...case.... python如何表达


3、 函数传参

a = 1
b = [2]
c = ['test']

def foo(x, y, z):
    x = 2
    y = 5
    z[0] = 3

foo(a, b, c)
print a, b, c


4、如何传递变长参数？

def function(*args, **kwargs):
    return


4、range()和xrange()的区别？


4、enumerate


4、字典结构、字典的key有什么限制，python哪些类型是可hash的


5、zip

有两个列表 
l1 = ['key1', 'key2', 'key3', 'key4']
l2 = [1, 2, 3, 4]

怎么得到字典{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4}

dict(zip(l1, l2))


5、如何判断对象的类型是str、tuple、dict或是list等？


5、如何判断一个对象是不是可迭代对象


5、迭代器和生成器


6、列表解析


6、lambda, filter, map, yield


6、提取range(100)中的奇数


7、list.reverse()、reversed(list)和list[::-1]的区别？

l =  range(10)
l.reverse()  # l 被翻转
reversed(l)  # 返回l的反向迭代器
l[::-1]      # 返回翻转的l的新对象


8、with的使用, 如何定义支持with语句的对象？


9、异常处理, 断言？

assert isinstance('aaa', str), 'tips'

try:
    pass
except (ValueError, ):
    pass
except Exception, e:
    raise
else:
    pass
finally:
    pass


9、类的三大特性, 简单举一个多态的例子？


10、实例方法、类方法、静态方法的区别，如何实现？


11、如何调用父类的方法？


12、静态变量、实例变量

class Foo(object):
    a = 1

obj = Foo()
obj.a += 2
print obj.a


class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
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


14、线程锁、多线程、多进程、协程，线程同步方法有哪些？


15、闭包、修饰器


16、元类，描述符


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
