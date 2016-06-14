# -*- coding: utf-8 -*-
"""
说到嗅探必须要讲到所支持的环境，并非只能对本机或者HUB环境才能使用。
对于交换机，你可以指定一个口为嗅探口，从这个口能拿到所有端口的数据。
如果这个交换是核心交换，那么你所能取到数据将更多。（三层交换一般都可以指定嗅探口）
1、如果你已经是个python爱好者你机器一定有了python的运行环境，
如果你没有可以到www.python.org去下载一个。我使用的还是python 2.3。
2、这段程序需要pcap模块支持，你可以到http://monkey.org/~dugsong/pypcap/去下载一个，
它有unix和win两个版本，请注意，win下他需要winpcap支持，如果你没有这个，请再下载winpcap。
同样，如果你是在unix下使用，请下载libpcap。
3、安装pcap没有太多说的，win下是个exe，直接运行。unix下直接make就可以了。
4、打开你的记事本，将以下代码保存在sniffer-QQ.py这个文件中。
"""
import struct
import pcap

pack = pcap.pcap()
pack.setfilter('udp')
key = ''
for recv_time, recv_data in pack:
   recv_len = len(recv_data)
   if recv_len == 102 and recv_data[42] == chr(02) and recv_data[101] == chr(03):
      print struct.unpack('>I', recv_data[49:53])[0]
      print '登陆了'
   elif recv_len == 55:
      print struct.unpack('>I',recv_data[49:53])[0]
      print '登陆了'


##如果你在*nix下运行,请将# -*- coding: cp936 -*-更改为# -*- coding: utf-8 -*-
##好了，你可以运行你的python程序了，试着登陆你的QQ。看你的QQ号码是否被抓下来了。
##这里付上我的抓屏结果
##D:\socket-qq>;sniffer-QQ.py
##278333853
##12345
##1234567890
##1234567890
##1234567890
##278333853
##1234567890
##1234567890
##278333853
##278333853
##
##
##利用的什么原理呢。
##QQ使用udp协议来和服务器进行通讯，当数据包在传输的时候。udp报文被抓了下来。而登陆包是以0x02开头0x03为结尾的，我们先判断是否为正确的登陆包，当然，登陆包的长度都为102个字节。我们取出结构中特定的位置，就是你的QQ号码了。
##如果还有什么疑问，请大家跟贴。
