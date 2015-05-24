#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""串口测试"""

__author__ = "baixue"


from time import sleep, clock
import struct
from binascii import hexlify, unhexlify, crc32
import serial


def hex_show_(data_hex):
    return data_hex.encode('hex')


def receive():
    com = serial.Serial('com4', 9600, timeout=10)
    com.flushInput()
    com.flushOutput()
    print com.timeout
    while True:
        start = clock()
##        print com.getCD()
##        print com.getCTS()
##        print com.getDSR()
##        print com.getRI()
##        n = com.inWaiting()
##        print n
##        data = com.read(n)
        data = com.readline()
        print len(data)
        print hexlify(data)
        print clock()-start
        sleep(1)

    com.close()

def send():
    com = serial.Serial('com4', 9600, timeout=10)
    com.flushInput()
    com.flushOutput()
    while True:
        start = clock()
        com.write(unhexlify('ff0102030405060708090Bff0A'))
        print clock()-start
        sleep(1)

    com.close()

if __name__ == "__main__":
    receive()
