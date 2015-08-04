#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# File: kinco.py
# Created: 11/09/2014 16:24:24
# Author: baixue
# Purpose:测试kinco-ED630驱动器的RS232的通讯
#------------------------------------------------------------------------------

import struct
from binascii import hexlify, unhexlify, crc32


def hex_show(data_hex):
    str_hex = ['%02x' % ord(i) for i in data_hex]
    return ''.join(str_hex)

def hex_show_(data_hex):
    return data_hex.encode('hex')

def strhex_to_data(strhex):
    if len(strhex)&1==0:
        return strhex.decode('hex')
    else:
        return (''.join((strhex[:-1], '0', strhex[-1])).decode('hex')

def hex_to_float(data):
    return struct.unpack(">f", data)[0]

def strhex_to_float(str_hex):
    return struct.unpack(">f", str_hex.decode('hex'))[0]

def float_to_strhex(data_float):
    return struct.pack(">f", data_float).encode('hex')

def to_hex(str_hex):
    str_list = str_hex.split(' ')

cmd = '01 2B 18 21 00 08 00 00 00'
cmdlst = cmd.split(' ')
print cmdlst
cmdint = [int(i, 16) for i in cmdlst]
chks = '%02x' % (-sum(cmdint)&0xffff)
cmdlst.append(chks[-2:])

print cmdlst

cmd = ''.join(cmdlst)
print cmd
cmd = cmd.decode('hex')



hexstr_ =  struct.pack('i', -109)
print hex_show(hexstr_)

hex(-109&0xff)
hex(109&0xff)
hex(-109&0xffffffff)

#cmd = ''.decode('hex')
