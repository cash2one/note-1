#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import select
import socket
import Queue

"""
通常 nonblocking模式, 如果socket没准备好的情况下, 试图用发送或接受数据, 对send()和recv()的调用
会产生socket.error异常
"""

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.setblocking(0)
sock_server.bind(('', 5555))
sock_server.listen(5)

inputs = [sock_server]
outputs = []
message_queues = {}


while True:
    print "waiting for next event"
    readable, writable, exceptional = select.select(inputs, outputs, [], 1.0)

    # when timeout reached, select return three empty lists
    if not (readable or writable or exceptional):
        print "Time out !"

    for s in readable:
        if s is sock_server:
            # a readable socket is ready to accept a connection
            conn, addr = s.accept()
            print " connection from", addr
            conn.setblocking(0)
            inputs.append(conn)
            message_queues[conn] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print "received: ", data, "from ", s.getpeername()
                message_queues[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print " closing"
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                # remove message queue
                del message_queues[s]

    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            print " ", s.getpeername(), 'queue empty'
            outputs.remove(s)
        else:
            print " sending ", next_msg, " to ", s.getpeername()
            s.send(time.asctime() + ' ' + next_msg)

    for s in exceptional:
        print " exception condition on ", s.getpeername()
        # stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        # Remove message queue
        del message_queues[s]
