#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import select


EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n' \
            b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n' \
            b'Hello, world!'

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(("0.0.0.0", 5555))
sock_server.listen(5)
sock_server.setblocking(0)

epoll = select.epoll()
epoll.register(sock_server.fileno(), select.EPOLLIN)

connections = {}
requests = {}
responses = {}

try:
    # #轮询注册的事件集合
    while True:
        events = epoll.poll(1)  # timeout = 1
        for fd, event in events:
            # 有新连接
            if fd == sock_server.fileno():
                conn, addr = sock_server.accept()
                conn.setblocking(0)
                epoll.register(conn.fileno(), select.EPOLLIN)
                connections[conn.fileno()] = conn
                requests[conn.fileno()] = b''
                responses[conn.fileno()] = response
            # 可读事件
            elif event & select.EPOLLIN:
                requests[fd] += connections[fd].recv(1024)
                if EOL1 in requests[fd] or EOL2 in requests[fd]:
                    # 修改读取到消息的连接到等待写事件集合
                    epoll.modify(fd, select.EPOLLOUT)
                    print('-' * 40 + '\n' + requests[fd].decode()[:-2])
            # 可写事件
            elif event & select.EPOLLOUT:
                byteswritten = connections[fd].send(responses[fd])
                responses[fd] = responses[fd][byteswritten:]
                if len(responses[fd]) == 0:
                    epoll.modify(fd, 0)
                    connections[fd].shutdown(socket.SHUT_RDWR)
            # 关闭事件
            elif event & select.EPOLLHUP:
                epoll.unregister(fd)
                connections[fd].close()
                del connections[fd]
finally:
    epoll.unregister(sock_server.fileno())
    epoll.close()
    sock_server.close()
