#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: serialport.py
# Created: 12/12/2013 15:31:12
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

from time import sleep
import serial
from worker import Worker


class SerialPort(object):
    
    def __init__(self):
        super(SerialPort, self).__init__()
        
        self.thread = MyThread(self.getData, ())


    def openCom(self, com):
        self.com = serial.Serial(com, 9600)
        self.com.flushInput()
        self.com.flushOutput()

    def write(self, data):
        self.com.write(data)

    def read(self):
        n = self.com.inWaiting()
        data = self.com.read(n)
        return data

    def close(self):
        self.com.close()

    def checksum(self, data):
        #计算校验码
        lst = [ord(i) for i in data]
        checksum = hex(sum(lst) & 255)[2:]
        return checksum, data+checksum+'\n'

    def checkData(self, data):
        #核对读回数据的校验码
        if self.checksum(data[0:-3])==data[-3:]:
            return True, float(data[1:-3])
        else:
            return False, 0.0
        
    def readI7017(self):
        data = self.com.read()
        ok, data = self.checkData(data)
        return data

    def writeI7017(self, data):
        checksum, data = self.checksum(data)
        self.write(data)

    def getData(self):
        self.write('data')
        sleep(0.1)
        return self.readI7017()
        



if __name__ == "__main__":
    com = SerialPort()
    print com.checksum('>+12.453')


