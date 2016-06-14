#!/usr/bin/env python
# -*- coding: utf-8 -*-


seq = ['one', 'two', 'three']

for i, element in enumerate(seq):
    seq[i] = '%d: %s' % (i, seq[i])

print seq

# ***************************************************************

seq = ['one', 'two', 'three']


def _treatment(pos, element):
    return '%d: %s' % (pos, element)

print [_treatment(i, el) for i, el in enumerate(seq)]

a = raw_input()
