#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import socket
import threading
from thread import start_new_thread


HOST = '0.0.0.0'
PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


try:
    sock.bind((HOST, PORT))
except socket.error as e:
    print e
    sys.exit()

sock.listen(5)  # 5 指等待处理的连接的最多数量


def client_thread(conn):
    remote_addr = conn.getpeername()
    while True:
        data = conn.recv(1024)
        if data:
            conn.send('[%s] %s' % (time.ctime(), data))
        else:
            # 客户端关闭连接后, 会收到一个空的消息(空字符串)
            break
    conn.close()
    print '%s:%s is done' % remote_addr


try:
    while True:
        print 'Waiting for connection...'
        conn, addr = sock.accept()
        assert isinstance(addr, tuple)
        print '%s:%s connected' % addr
        t = threading.Thread(target=client_thread, args=(conn,))
        t.daemon = True
        t.start()
        # start_new_thread(client_thread, (conn,))
finally:
    sock.close()
