#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import socket
import select
import Queue

# windows不支持poll

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setblocking(0)
server.bind(('', 5555))
server.listen(5)

message_queues = {}

READ_ONLY = (select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
READ_WRITE = (READ_ONLY | select.POLLOUT)

poll = select.poll()
poll.register(server, READ_ONLY)

fd_to_socket = {server.fileno(): server}

while True:
    print "Waiting for the next event..."
    events = poll.poll(1000)  # 1000ms
    print "*" * 20
    print events
    print "*" * 20
    for fd, flag in events:
        s = fd_to_socket[fd]
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # A readable socket is ready to accept a connection
                conn, addr = s.accept()
                print "Connection ", addr
                conn.setblocking(0)

                fd_to_socket[conn.fileno()] = conn
                poll.register(conn, READ_ONLY)

                message_queues[conn] = Queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    print "received %s from %s " % (data, s.getpeername())
                    message_queues[s].put(data)
                    poll.modify(s, READ_WRITE)
                else:
                    print "closing", s.getpeername()
                    poll.unregister(s)
                    s.close()
                    del message_queues[s]
        elif flag & select.POLLHUP:
            # A client that "hang up", to be closed.
            print "Closing ", s.getpeername(), "(HUP)"
            poll.unregister(s)
            s.close()
        elif flag & select.POLLOUT:
            # Socket is ready to send data , if there is any to send
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                # No messages waiting so stop checking
                print s.getpeername(), " queue empty"
                poll.modify(s, READ_ONLY)
            else:
                print "sending %s to %s" % (next_msg , s.getpeername())
                s.send(time.asctime() + ' ' + next_msg)
        elif flag & select.POLLERR:
            # Any events with POLLERR cause the server to close the socket
            print "exception on", s.getpeername()
            poll.unregister(s)
            s.close()
            del message_queues[s]
