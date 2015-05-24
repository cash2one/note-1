#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: serialport.py
# Created: 08/01/2014 14:30:18
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

import struct
from time import sleep
import serial
from worker import Worker


class SerialPort(object):
    
    def __init__(self):
        super(SerialPort, self).__init__()
        
        self.thread = MyThread(self.getData, ())


    def openCom(self, com):
        self.com = serial.Serial(com, 9600, timeout=10)
        #读取函数超时不会发生异常,而是返回了一个字符串
        self.com.flushInput()
        self.com.flushOutput()

    def write(self, data):
        self.com.write(data)

    def read(self, n):
        data = self.com.read(n)
        return data

    def readAll(self):
        n = self.com.inWaiting()
        data = self.com.read(n)
        return data

    def close(self):
        self.com.close()

    def getData(self):
        cmd = 'AA5508F7000101FE0901'.decode('hex')
        self.write(cmd)
        data = self.com.read(14)
        if len(data)<14:
            raise IOError, 'SerialPort Error'
        else:
            return struct.unpack('f',data[8:-2])[0], data


