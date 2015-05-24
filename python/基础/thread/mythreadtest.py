#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep, ctime
from myThread import MyThread


def loop(a,b,c):
    print 'start loop at:', ctime()
    sleep(1)
    print 'loop done at:', ctime()
    return a+b+c
    
def main():
    t = MyThread(loop, (1,2,3))
    t.start()
    print 'wait....', ctime()
    sleep(0.5)
    print 'wait....', ctime()
    t.join()#等待线程结束
    print t.getResult(), ctime()



if __name__ == "__main__":
    main()
