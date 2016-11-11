#!/usr/bin/env python
# -*- coding: utf-8 -*-

####################################################################
# python 自动重启本程序
####################################################################

import time
import sys
import os


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    print 'start...'
#  answer = raw_input("Do you want to restart this program ? ")
#  if answer.strip() in "y Y yes Yes YES".split():
#    restart_program()
    print "3秒后,程序将结束..."
    time.sleep(3)
    restart_program()

