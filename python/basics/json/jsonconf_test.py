#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def read_json_conf(path):
    fobj = open(path, 'r')
    text = fobj.read()
    fobj.close()
    # conf = json.load(fobj)
    conf = json.loads(text)
    return conf

if __name__ == '__main__':
    conf = read_json_conf('config.json')
    print type(conf)
    print conf["Global_Settings"]
    print '-------------------------------------------------------'
    print conf["Redis_Settings"]
    print '-------------------------------------------------------'
    print conf["Store_Settings"]
    print '-------------------------------------------------------'
    print conf["Spider_Settings"]
    print '-------------------------------------------------------'
    print conf["Item_Order"]
    print '-------------------------------------------------------'
    print conf["Item_Define"]
    print conf["Item_Define"].keys()
