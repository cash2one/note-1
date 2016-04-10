# -*- coding: utf-8 -*-

"""
用Python subprocess开启redis-server
"""

import gevent
from subprocess import Popen, PIPE


def work_a():
    while True:
        print('work_a')
        gevent.sleep(1)

work_a = gevent.spawn(work_a)

f = Popen(['redis-server'], stdout=PIPE).stdout


for i in range(10):
    print i
    print f.readline()
    gevent.sleep(1)

f.close()

# popen.send_signal(signal.SIGTERM)  # 向子进程发送信号
# popen.terminate()

gevent.sleep(5)

work_a.kill()
