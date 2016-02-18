#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Delete the file specified type in the directory

"""

__author__ = 'Pysaoke'

import os
import argparse
from termcolor import colored


def del_type_file(directory, ftype):
    for rel_path in os.listdir(directory):
        abs_path = os.path.join(directory, rel_path)
        if os.path.isdir(abs_path):
            del_type_file(abs_path, ftype)  # callback self
        elif os.path.isfile(abs_path):
            extname = get_extname(abs_path)
            if extname in ftype:
                os.remove(abs_path)
                print colored("REMOVE >>> ", 'red'), colored(abs_path, 'green')


def get_extname(fname):
    return os.path.splitext(fname)[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ftype", nargs='+', help="the extension name of file: *.pyc; *.txt")
    parser.add_argument("-d", "--dir", help="directory: default:current directory")
    args = parser.parse_args()

    ftype = args.ftype
    ftype = map(get_extname, ftype)
    ftype = filter(lambda s: s and s.strip(), ftype)  # 过滤掉空字符

    assert len(ftype) > 0, "ERROR:file error"

    directory = os.path.curdir if not args.dir or args.dir=='.' else args.dir

    assert os.path.exists(directory), "ERROR:%s is not exist"

    del_type_file(directory, ftype)
