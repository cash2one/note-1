#!/usr/bin/env python
# -*- coding: utf-8 -*-

"debug camera"

__author__ = "baixue"

from ctypes import *
import os, sys
from time import sleep
from binascii import unhexlify
import serial


DIR_ROOT = os.getcwd()

HEADER = 'AABB'
ADDR = '01'
RELAY_NO = ['%02d' % (i+1) for i in range(16)]

# config camera info
GROUP_A = (('01', '02'),
           ((12461150, 'L1'), (12442173, 'R1')),
           os.path.join(DIR_ROOT, u'A组相机'.encode('gbk')),
           u'第一组相机')
GROUP_B = (('03', '04'),
           ((12461130, 'L1'), (12492601, 'R1')),
           os.path.join(DIR_ROOT, u'B组相机'.encode('gbk')),
           u'第二组相机')
GROUP_C = (('05',),
           ((12461145, 'L1'), (13020874, 'R1')),
           os.path.join(DIR_ROOT, u'C组相机'.encode('gbk')),
           u'第三组相机')
CAMERA = (GROUP_A, GROUP_B, GROUP_C)


dll = cdll.LoadLibrary('GrabImage32_dll.dll')

def GrabImage(serialNum, path, imageName, shutter=47.574, gain=0.0, sleepTime=0, numImages=1):
   serialNum = c_uint(serialNum)
   strPath = c_char_p(path)
   imageName = c_char_p(imageName)
   shutter = c_float(shutter)
   gain = c_float(gain)
   sleepTime = c_int(sleepTime)
   numImages = c_int(numImages)
   ret = dll.GrabImage(serialNum, path, imageName, shutter, gain, sleepTime, numImages)
   return ret

def create_dir():
    for group in CAMERA:
       image_dir = group[2]
       if not os.path.exists(image_dir):
          os.mkdir(image_dir)

def getPortList():
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) <= 0:
        # the serial port can't find!
        return 0
    else:return [i[0] for i in port_list]

def generate_relay_cmd(relayNo, state=False):
    if relayNo in RELAY_NO:
        cmd = ''.join((HEADER, ADDR, relayNo, '01' if state else '00'))
    elif relayNo == 'AllOpen':
        cmd = ''.join((HEADER, ADDR, '1A01'))
    elif relayNo == 'AllClose':
        cmd = ''.join((HEADER, ADDR, '1C01'))
    else:raise TypeError('parameter-relayNo is not correct')
    chks = '%02x' % (sum(bytearray(unhexlify(cmd)))%256)
    return cmd+chks
    
def main():
    # create dir if non_exist
    create_dir()

    # check serial port
    if getPortList==0:
        print u'没有可用串口'
        raw_input('按ENTER键退出...'.decode('utf-8').encode('gbk'))
        return None

    com = serial.Serial('com2', 9600, timeout=5)
    com.flushInput()
    com.flushOutput()
    com.write(unhexlify(generate_relay_cmd('AllClose')))

    for group in CAMERA:
        print group[3]
        for light in group[0]:
           com.write(unhexlify(generate_relay_cmd(light, True)))
        sleep(0.5)
        for camera in group[1]:
           ret = GrabImage(camera[0], group[2], camera[1])
        for light in group[0]:
           com.write(unhexlify(generate_relay_cmd(light, False)))
        print

    com.write(unhexlify(generate_relay_cmd('AllClose')))
    com.close()
    print u'完成!'
    raw_input('按ENTER键退出...'.decode('utf-8').encode('gbk'))
    return None

if __name__ == "__main__":
    main()
    sys.exit()
