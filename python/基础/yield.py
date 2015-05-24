#!/usr/bin/env python
# -*- coding: utf-8 -*-

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






















if __name__ == "__main__":
    pass
