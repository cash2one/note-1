#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import socket


sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sock_server.bind(('', 5555))
except socket.error as e:
    print e
    sys.exit()

sock_server.listen(5)

try:
    while True:
        print 'Waiting for connection...'
        sock_cli, addr = sock_server.accept()
        print '%s:%s connected' % addr

        while True:
            try:
                sock_cli.sendall(time.asctime() + '\n')
            except Exception as e:
                print e
                break
            time.sleep(1)

        sock_cli.close()
        print '%s:%s disconnected' % addr
finally:
    sock_server.close()
