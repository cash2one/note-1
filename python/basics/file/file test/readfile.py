# -*- coding: utf-8 -*-

"""
read and display text file
"""

# get filename
filename = raw_input('Enter filename:')
print

# attempt to open file for reading
try:
    fd = open(filename, 'r')
except IOError as e:
    print "***file open error:", e
else:
    # display contents to the screen
    for line in fd:
        print line

print
print "Done!"

raw_input()
