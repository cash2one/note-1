#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ConfigParser import ConfigParser

CONFIGFILE = "config.txt"

config = ConfigParser()

#读取配置文件
config.read(CONFIGFILE)

#打印初始问候语
#要查看的区段是'messages'
print config.get('messages', 'greeting')

#打印配置文件中的结果信息
#以逗号结束，以在同一行显示
print config.get('messages', 'result_message')

#getfloat()将config值转换为float类型
print config.getfloat('numbers', 'pi')

config.set('numbers', 'pi', 4.001)

config.add_section('new_section')
config.set('new_section', 'radius', '12.5')

with open('config.txt', 'wb') as configfile2:
    config.write(configfile2)

with open('config.cfg', 'wb') as configfile1:
    config.write(configfile1)
