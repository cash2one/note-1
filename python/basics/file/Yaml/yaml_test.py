#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


f = open("test3.yaml", 'r')

data = yaml.load(f)

print data
print
print data['Tracy']['family']
print
print data['Tracy']['family']['children']
print
print data['Tracy']['address']['city']
print
print data['Vince']['address']['city']

f.close()

f = open("test3_dup.yaml", 'w')

yaml.dump(data, f)

f.close()

raw_input('press enter...')
