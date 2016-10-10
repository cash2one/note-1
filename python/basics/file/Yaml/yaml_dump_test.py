#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

f = open("dup_test.yaml", 'w')

dic = {
    'baixue': 18, 'nginx': 20, 'apache': 'webserver'
}

yaml.dump(range(10), f)
yaml.dump(dic, f)

f.close()
