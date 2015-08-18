# -*- coding: utf-8 -*-

lstA = [1,2,3,4]
lstB = [ x**2 for x in lstA]
print lstB

print [i for i in range(10) if i%2 == 0]


print 'new-----------------------------------'
print ['even' for i in range(10) if i%2==0]