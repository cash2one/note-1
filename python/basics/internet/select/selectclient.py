#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, sys, select

"""Noblocking I/O with select()"""

port = 5555
host = 'localhost'

spinsize = 10
spinpos = 0
spindir = 1


def spin():
    global spinsize, spinpos, spindir
    spinstr = '.' * spinpos + '|' + '.' * (spinsize - spinpos - 1)
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


try:
    while True:
        infds, outfds, errfds = select.select([s], [], [s], 0.1)

        if infds:
            data = s.recv(4096)
            if not data:
                print ("\rRemote end closed connect; exiting.")
                break
            sys.stdout.write("\rReceived: " + data)
            sys.stdout.flush()

        if errfds:
            print "\rProblem occurred; exiting."
            sys.exit(0)
        spin()
finally:
    s.close()
