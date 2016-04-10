# -*- coding: utf-8 -*-

"""
Python标准库子进程测试
如果用标准库启动子进程,gevent停止运行后,子进程开启的程序仍然运行.
如果用gevent.subprocess运行子进程,那么gevent结束后,子进程开启的程序也停止
"""

import gevent
from subprocess import Popen, PIPE

import signal


def cron():
    while True:
        print('cron')
        gevent.sleep(1)

g = gevent.spawn(cron)

f = Popen(['ping', 'www.baidu.com'], stdout=PIPE).stdout


for i in range(10):
    print i
    print f.readline()
    gevent.sleep(1)

f.close()

# popen.send_signal(signal.SIGTERM)  # 向子进程发送信号
# popen.terminate()

gevent.sleep(5)

g.kill()
