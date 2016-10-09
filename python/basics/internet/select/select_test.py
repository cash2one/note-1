#!/usr/bin/env python
# -*- coding: utf-8 -*-
import select
import socket
import Queue


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)

addr = ('', 5001)
server.bind(addr)
server.listen(10)

inputs = [server]
outputs = []
message_queues = {}

timeout = 20

while inputs:
    print "waiting for next event"
    readable, writable, exceptional = select.select(inputs, outputs, timeout)

    # when timeout reached, select return three empty lists
    if not (readable or writable or exceptional):
        print "Time out !"

    for s in readable:
        if s is server:
            # a "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print " connection from", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.queue()
        else:
            data = s.recv(1024)
            if data:
                print " received", data, "from ", s.getpeername()
                message_queues[s].put(data)
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print " closing", client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close(s)
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
            s.send(next_msg)
     
    for s in exceptional:
        print " exception condition on ", s.getpeername()
        # stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        # Remove message queue
        del message_queues[s]
