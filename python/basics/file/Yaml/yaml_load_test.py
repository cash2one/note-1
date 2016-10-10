#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

f = open("test2.yaml", 'r')

data = yaml.load(f)

print data
print
print data['family']['parents']

f.close()
