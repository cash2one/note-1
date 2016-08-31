# -*- coding: utf-8 -*-
import gevent
from gevent.event import Event, AsyncResult


evt = Event()


def setter():
    """After 3 seconds, wake all threads waiting on the value of evt"""
    print('A: Hey wait for me, I have to do something')
    gevent.sleep(3)
    print("Ok, I'm done")
    evt.set()


def waiter():
    """After 3 seconds the get call will unblock"""
    print("I'll wait for you")
    evt.wait()  # blocking
    print("It's about time")


# 事件可以通知很多worker
def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
    ])


"""
事件对象的一个扩展是AsyncResult,它允许你在唤醒调用上附加一个值.
它有时也被称作是future或defered,因为它持有一个指向将来任意时间可设置 为任何值的引用.
"""

a = AsyncResult()


def setter1():
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    a.set('Hello!')


def waiter1():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(a.get())


gevent.joinall([
    gevent.spawn(setter1),
    gevent.spawn(waiter1),
])


if __name__ == '__main__':
    main()
