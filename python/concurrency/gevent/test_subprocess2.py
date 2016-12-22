# -*- coding: utf-8 -*-
import gevent
from subprocess import Popen, PIPE

import signal


def cron():
    while True:
        print('cron')
        gevent.sleep(1)

g = gevent.spawn(cron)

popen = Popen(['ping', 'www.baidu.com'], stdout=PIPE)

# f = popen.stdout
# for i in range(10):
#     print i
#     print f.readline()
#     gevent.sleep(1)

# f.close()

# print popen.communicate()  # 等待子进程结束, 返回标准输出. 会阻塞主进程

# popen.send_signal(signal.SIGTERM)  # 向子进程发送信号

print popen.terminate()

gevent.sleep(5)

g.kill()
