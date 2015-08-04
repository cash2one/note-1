#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------

import socket, sys, select

port = 5001
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1

def spin():
    global spinsize, spinpos, spindir
    spinstr = '.' * spinpos + '|' + '.' * (spinsize-spinpos-1)
    sys.stdout.write('\r' + spinstr + ' ')
    sys.stdout.flush()

    spinpos += spindir
    if spinpos < 0:
        spindir = 1
        spinpos = 0
    elif spinpos >= spinsize:
        spinpos -= 2
        spindir = -1

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

while 1:
    infds, outfds, errfds = select.select([s], [], [s], 0.1)
    if len(infds):
        data = s.recv(4096)
        if not len(data):
            print ("\rRemote end closed connect; exiting.")
            break
        sys.stdout.write("\rReceived: " + data)
        sys.stdout.flush()
    if len(errfds):
        print "\rProblem occurred; exiting."
        sys.exit(0)
    spin()
