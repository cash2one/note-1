#!/usr/bin/env python
# -*- coding: utf-8 -*-
import select
import socket


class PollServer(object):
    stdmask = select.POLLERR | select.POLLHUP | select.POLLNVAL

    def __init__(self, sock):
        self.poll = select.poll()
        self.mastersock = sock
        self.watch_read(sock)
        self.buffers = {}
        self.sockets = {sock.fileno(): sock}

    def fd2socket(self, fd):
        return self.sockets[fd]

    def watch_read(self, fd):
        self.poll.register(fd, select.POLLIN | self.stdmask)

    def watch_write(self, fd):
        self.poll.register(fd, select.POLLOUT | self.stdmask)

    def watch_both(self, fd):
        self.poll.register(fd, select.POLLIN | select.POLLOUT | self.stdmask)

    def dont_watch(self, fd):
        self.poll.unregister(fd)

    def new_conn(self, sock):
        fd = sock.fileno()
        self.watch_both(fd)
        self.buffers[fd] = 'Welcome to the EchoServer, %s\n' % str(sock.getpeername())
        self.sockets[fd] = sock

    def read_event(self, fd):
        try:
            self.buffers[fd] += self.fd2socket(fd).recv(4096)
        except Exception as e:
            print e
            self.closeout(fd)
        self.watch_both(fd)

    def write_event(self, fd):
        if not self.buffers[fd]:
            self.watch_read(fd)
            return
        try:
            bytes_written = self.fd2socket(fd).send(self.buffers[fd])
        except Exception as e:
            print e
            self.closeout(fd)

        self.buffers[fd] = self.buffers[fd][bytes_written:]

        if not self.buffers[fd]:
            self.watch_read(fd)

    def error_event(self, fd):
        self.closeout(fd)

    def closeout(self, fd):
        self.dont_watch(fd)
        try:
            self.fd2socket(fd).close()
        except Exception as e:
            print e
        del self.buffers[fd]
        del self.sockets[fd]

    def serve_forever(self):
        while True:
            results = self.poll.poll()
            for fd, event in results:
                if fd == self.mastersock.fileno() and event == select.POLLIN:
                    try:
                        newsock, addr = self.fd2socket(fd).accept()
                        newsock.setblocking(0)
                        print 'Got connection from ', newsock.getpeername()
                        self.new_conn(newsock)
                    except Exception as e:
                        print e
                elif event == select.POLLIN:
                    self.read_event(fd)
                elif event == select.POLLOUT:
                    self.write_event(fd)
                else:
                    self.error_event(fd)


if __name__ == "__main__":
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_server.bind(('', 5555))
    sock_server.setblocking(0)
    sock_server.listen(5)

    server = PollServer(sock_server)
    server.serve_forever()
