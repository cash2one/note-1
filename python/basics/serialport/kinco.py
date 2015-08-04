#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: kinco.py
# Created: 11/09/2014 16:24:24
# Author: baixue
# Purpose:测试kinco-ED630驱动器的RS232的通讯
#------------------------------------------------------------------------------

from time import sleep
import serial

CMDS = []


def hexShow(datahex):
    dataint = ['%02x' % ord(i) for i in datahex]
    return ''.join(dataint)

def join_chks(cmd):
    cmdlist = cmd.split(' ')
    cmdint = [int(i, 16) for i in cmdlist]
    chks = '%02x' % (-sum(cmdint)&0xFFFF)
    cmdlist.append(chks[-2:])
    return ''.join(cmdlist)

def calc_chks(cmdlist):
    cmdint = [int(i, 16) for i in cmdlist]
    chks = '%02x' % (-sum(cmdint)&0xffff)
    cmdlist.append(chks[-2:])
    return ''.join(cmdlist)

com = serial.Serial('com1', 9600, timeout=5)

com.flushInput()
com.flushOutput()

cmd = '01 2B 18 21 00 31 00 00 00'
#com.write(join_chks(cmd).decode('hex'))
cmd = cmd.split(' ')

ID = raw_input('Please input device id:')

cmd[0] = ID

while True:
    addr = raw_input('Please input program no:')
    if addr == 'exit':
        break
    cmd[5] = addr
    com.write(calc_chks(cmd).decode('hex'))
    data = com.read(20)
    print data
    print data[11] #60h成功, 80h失败
    print hexShow(data)


#sleep(0.1)

com.close()


##if __name__ == "__main__":
##    pass
