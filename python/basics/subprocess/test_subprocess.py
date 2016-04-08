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

sub = Popen(['ping crm.100credit.cn'], shell=True, stdout=PIPE, stderr=PIPE)


for i in range(50):
	print sub.stdout.read()
	gevent.sleep(1)


sub.send_signal(signal.SIGTERM) # 向子进程发送信号
sub.terminate()

g.kill()
