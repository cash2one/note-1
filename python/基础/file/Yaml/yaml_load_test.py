#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Doc String'''

__author__ = 'baixue'

import yaml

f = open("test2.yaml", 'r')

data = yaml.load(f)

print data
print
print data['family']['parents']

f.close()

#yaml.dump(data)







if __name__ == "__main__":
    pass
