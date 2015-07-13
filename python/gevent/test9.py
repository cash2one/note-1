#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
程序停止
当主程序(main program)收到一个SIGQUIT信号时，不能成功做yield操作的Greenlet可能会令意外地挂起程序的执行。
这导致了所谓的僵尸进程， 它需要在Python解释器之外被kill掉。
'''


import gevent
import signal

def run_forever():
    gevent.sleep(1000)

if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()