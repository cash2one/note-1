#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading


class Worker(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name=name
        self.func=func
        self.args=args
        self.daemon = True # 设为守护线程,确保应用程序退出时，线程也能随之安全退出

    def getResult(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)

#用start()来启动线程
#用join()来等待线程结束
#用getResult()来获取函数结果
