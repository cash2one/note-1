#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Delete the file the specified type in the directory

"""

__author__ = 'Pysaoke'

import os
import argparse
from termcolor import colored


def del_type_file(dir, ftype):
    for rel_path in os.listdir(dir):
        abs_path = os.path.join(dir, rel_path)
        if os.path.isdir(abs_path):
            del_type_file(abs_path, ftype)
        elif os.path.isfile(abs_path):
            extname = get_file_extname(abs_path)
            if extname in ftype:
                os.remove(abs_path)
                print colored("REMOVE >>>",'red'), colored(abs_path,'green')

def get_file_extname(fname):
    ext = os.path.splitext(fname)
    return ext[1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ftype", nargs='+', help="the extension name of file:*.pyc;*.txt")
    parser.add_argument("-d", "--dir", help="directory: default--curdir")
    args = parser.parse_args()

    ftype = args.ftype
    ftype = map(get_file_extname, ftype)
    directory = os.path.curdir if not args.dir or args.dir=='.' else args.dir

    assert os.path.exists(directory), "ERROR:%s is not dir"
    del_type_file(directory, ftype)