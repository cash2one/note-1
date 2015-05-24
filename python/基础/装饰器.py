#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""template.py --- docstring"""

from time import ctime, sleep


def tsfunc(func):
    def wrappendFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappendFunc

@tsfunc
def foo():
    print'i am foo'
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()


##if __name__ == '__main__':
##    pass
