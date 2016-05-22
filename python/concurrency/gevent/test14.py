# -*- coding: utf-8 -*-

"""
gevent子进程测试
"""

import gevent
from gevent.subprocess import Popen, PIPE

import signal


def cron():
    while True:
        print('cron')
        gevent.sleep(1)

g = gevent.spawn(cron)

popen = Popen(['ping', 'www.baidu.com'], stdout=PIPE)


for i in range(10):
    print i
    print popen.stdout.readline()
    gevent.sleep(1)

# popen.send_signal(signal.SIGTERM)  # 向子进程发送信号
# popen.terminate()

while True:
    print 'run...'
    gevent.sleep(1)

# g.kill()
