#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import gevent
from gevent.subprocess import Popen, PIPE


def cron():
    while True:
        print('cron')
        gevent.sleep(1)

g = gevent.spawn(cron)

sub = Popen(['ping', 'www.baidu.com', '-c', '5'], stdout=PIPE, stderr=PIPE)


# for i in range(10):
# 	print sub.stdout.readline()
# 	gevent.sleep(1)

# try:
# 	print sub.communicate(timeout=5)  # 会阻塞主进程， 但不会阻塞协程的worker
# except gevent.Timeout:
# 	print 'timeout error'

# print sub.poll()

# if not sub.poll():
# 	# sub.send_signal(signal.SIGTERM)  # 向子进程发送信号
# 	sub.terminate()

print sub.poll()

while sub.poll() is None:
	print '------------'
	print sub.stdout.readline()
	print '------------'
	gevent.sleep(1)

print 'return', sub.poll()

gevent.sleep(5)

g.kill()
