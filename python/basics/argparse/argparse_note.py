#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
argparse是python用于解析命令行参数和选项的标准模块, 用于代替已经过时的optparse模块.
"""

import argparse


# Positional arguments


parser = argparse.ArgumentParser(description="new a python module")
parser.add_argument("square", default=0, type=int, help="display a square of a given number")
args = parser.parse_args()
print args.square**2

# add_argument 说明

# 不带'--'的参数
# 调用脚本时必须输入值
# 参数输入的顺序与程序中定义的顺序一致

# '-'的参数
# 可不输入    add_argument("-a")
# 类似有'--'的shortname，但程序中的变量名为定义的参数名

# '--'参数
# 参数别名: 只能是1个字符，区分大小写


# 多个参数 nargs='+'
parser = argparse.ArgumentParser(description="new some python module")
parser.add_argument("fname", nargs='+', type=str,
                    help="the name of python module file")
args = parser.parse_args()
print args.fname


# Optional arguments


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print "verbosity turned on"


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
   print "verbosity turned on"


# Short options


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print "verbosity turned on"


# Combining Positional and Optional arguments


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print "the square of {} equals {}".format(args.square, answer)
else:
    print answer


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display the square of a given number")
parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print "{}^2 == {}".format(args.square, answer)
else:
    print answer
