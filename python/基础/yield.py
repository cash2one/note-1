#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------迭代器(Iterator)-------------------------#
'''
当创建一个列表(list)时，你可以逐个的读取每一项，这就叫做迭代（iteration）。
'''
mylist = [1, 2, 3]
for i in mylist:
    print i
'''
Mylist就是一个迭代器，不管是使用复杂的表达式列表，还是直接创建一个列表，都是可迭代的对象。
'''
mylist = [x*x for x in range(3)]
for i in mylist:
    print i
'''
你可以使用“for··· in ···”来操作可迭代对象,
如：list,string,files,这些迭代对象非常方便我们使用,因为你可以按照你的意愿进行重复的读取。
但是你不得不预先存储所有的元素在内存中，那些对象里有很多元素时，并不是每一项都对你有用。
'''

#-------------------------生成器(Generators)-------------------------#
'''
生成器同样是可迭代对象，但是你只能读取一次，因为它并没有把所有值存放内存中，它动态的生成值：
'''
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print i
'''
使用()和[]结果是一样的,
但是,第二次执行"for in mygenerator"不会有任何结果返回,因为它只能使用一次.
首先计算0,然后计算1,之后计算4,依次类推.
'''

#-------------------------Yield-------------------------#
'''Yield是关键字， 用起来像return，yield在告诉程序，要求函数返回一个生成器.'''
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator()
# create a generator
print mygenerator  # <generator object createGenerator at 0xb7555c34>
# mygenerator is an object!

for i in mygenerator:
    print i
'''
这个示例本身没什么意义，但是它很清晰地说明函数将返回一组仅能读一次的值,
要想掌握yield，首先必须理解的是:当你调用生成器函数的时候，如上例中的createGenerator(),
程序并不会执行函数体内的代码,它仅仅只是返回生成器对象，这种方式颇为微妙.
函数体内的代码只有直到每次循环迭代(for)生成器的时候才会运行.

函数第一次运行时，它会从函数开始处直到碰到yield时，就返回循环的第一个值，然后，交互的运行、返回，直到没有值返回为止.
如果函数在运行但是并没有遇到yield，就认为该生成器是空，原因可能是循环终止，或者没有满足任何"if/else".

接下来读一小段代码来理解生成器的优点：
'''
# 控制生成器穷举
class Bank():
# 创建银行,构造ATM机
    crisis = False
    def create_atm(self):
        while not self.crisis:
            yield "$100"

hsbc = Bank()
# 没有危机时，你想要多少，ATM就可以吐多少
corner_street_atm = hsbc.create_atm()
print corner_street_atm.next()
print corner_street_atm.next()
print [corner_street_atm.next() for cash in range(5)]
hsbc.crisis = True
# 危机来临，银行没钱了
print corner_street_atm.next()  # <type 'exceptions.StopIteration'>

wall_street_atm = hsbc.ceate_atm()
# 新建ATM，银行仍然没钱
print corner_street_atm.next()  # <type 'exceptions.StopIteration'>

hsbc.crisis = False 
# 麻烦就是，即使危机过后银行还是空的
print corner_street_atm.next()  # <type 'exceptions.StopIteration'>

brand_new_atm = hsbc.create_atm()
# 构造新的ATM，恢复业务
for cash in brand_new_atm:
    print cash

# 对于访问控制资源，生成器显得非常有用


#-------------------------迭代工具，你最好的朋友-------------------------#
'''
迭代工具模块包含了操做指定的函数用于操作迭代器。
想复制一个迭代器出来？链接两个迭代器？
以one liner（这里的one-liner只需一行代码能搞定的任务)用内嵌的列表组合一组值？
不使用list创建Map/Zip？···，
你要做的就是 import itertools，举个例子吧:
'''
# 四匹马赛跑到达终点排名的所有可能性：
horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print races  # <itertools.permutations object at 0xb754f1dc>
print list(itertools.permutations(horses))


#-------------------------理解迭代的内部机制：-------------------------#
'''
迭代(iteration)就是对可迭代对象(iterables,实现了__iter__()方法)和迭代器(iterators,实现了__next__()方法)的一个操作过程.
可迭代对象是任何可返回一个迭代器的对象,迭代器是应用在迭代对象中迭代的对象,
换一种方式说的话就是:iterable对象的__iter__()方法可以返回iterator对象,
iterator通过调用next()方法获取其中的每一个值.
'''



'''
yield 测试:
yield 的作用就是把一个函数变成一个 generator，
带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator.
调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
于是函数继续执行，直到再次遇到 yield.
'''

__author__ = 'baixue'


# 生成斐波那契数列
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

lst = list(fab(5))
print lst

for n in fab(5):
    print n

# 也可以手动调用fab(5)的next()方法, 因为fab(5)是一个generator对象，该对象具有next()方法
f = fab(5)
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
# 当函数执行结束时，generator 自动抛出StopIteration异常，表示迭代完成.
# 在for循环里，无需处理StopIteration异常，循环会正常结束.

#------------------总结----------------------#
# 一个带有 yield 的函数就是一个 generator，它和普通函数不同,
# 生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
# 虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：

#-----------------判断函数是不是generator-------------------#
from inspect import isgeneratorfunction
print isgeneratorfunction(fab) # 如果是, 返回True

#-----------------return的作用-----------------#
# 在一个 generator function 中，如果没有 return，则默认执行至函数完毕，
# 如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。


'''
协程 又称微线程, 纤程, Coroutine
'''


import time

# 基于协程的生产者消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)


# Python通过yield提供了对协程的基本支持, 但是不完全.
# 而第三方的gevent为Python提供了比较完善的协程支持
# 使用gevent，可以获得极高的并发性能，但gevent只能在Unix/Linux下运行.
# 在Windows下不保证正常安装和运行