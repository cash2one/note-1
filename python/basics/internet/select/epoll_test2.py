#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import select
import Queue


sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(("0.0.0.0", 8080))
sock_server.listen(1)
sock_server.setblocking(0)

epoll = select.epoll()
epoll.register(sock_server.fileno(), select.EPOLLIN)

message_queues = {}
fd_to_socket = {sock_server.fileno(): sock_server}

while True:
    print "等待活动连接......"
    # 轮询注册的事件集合
    events = epoll.poll(1)
    if not events:
        print "epoll超时无活动连接, 重新轮询......"
        continue

    print "有", len(events), "个新事件, 开始处理......"
    for fd, event in events:
        socket = fd_to_socket[fd]
        # 可读事件
        if event & select.EPOLLIN:
            # 如果活动socket为服务器所监听, 有新连接
            if socket == sock_server:
                connection, address = sock_server.accept()
                print "新连接：", address
                connection.setblocking(0)
                # 注册新连接fd到待读事件集合
                epoll.register(connection.fileno(), select.EPOLLIN)
                fd_to_socket[connection.fileno()] = connection
                message_queues[connection] = Queue.Queue()
            # 否则为客户端发送的数据
            else:
                data = socket.recv(1024)
                if data:
                    print "收到数据：", data, "客户端：", socket.getpeername()
                    message_queues[socket].put(data)
                    # 修改读取到消息的连接到等待写事件集合
                    epoll.modify(fd, select.EPOLLOUT)
        # 可写事件
        elif event & select.EPOLLOUT:
            try:
                msg = message_queues[socket].get_nowait()
            except Queue.Empty:
                print socket.getpeername(), " queue empty"
                epoll.modify(fd, select.EPOLLIN)
            else:
                print "发送数据：", msg , "客户端：", socket.getpeername()
                socket.send(msg)
        # 关闭事件
        elif event & select.EPOLLHUP:
            epoll.unregister(fd)
            fd_to_socket[fd].close()
            del fd_to_socket[fd]

epoll.unregister(sock_server.fileno())
epoll.close()
sock_server.close()
