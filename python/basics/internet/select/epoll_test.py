#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import select
import Queue


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_addr = ("192.168.1.5", 8080)
server.bind(server_addr)
server.listen(1)
print "服务器启动成功，监听IP：" , server_addr

server.setblocking(0)

timeout = 10
# 新建epoll事件对象, 后续要监控的事件添加到其中
epoll = select.epoll()
# 添加服务器监听fd到等待读事件集合
epoll.register(server.fileno(), select.EPOLLIN)
message_queues = {}

fd_to_socket = {server.fileno():server, }
while True:
    print "等待活动连接......"
    # 轮询注册的事件集合
    events = epoll.poll(timeout)
    if not events:
        print "epoll超时无活动连接，重新轮询......"
        continue
    print "有", len(events), "个新事件，开始处理......"
    for fd, event in events:
        sock = fd_to_socket[fd]
        # 可读事件
        if event & select.EPOLLIN:
            # 如果活动socket为服务器所监听, 有新连接
            if sock == server:
                connection, addr = server.accept()
                print "新连接：" , addr
                connection.setblocking(0)
                # 注册新连接fd到待读事件集合
                epoll.register(connection.fileno(), select.EPOLLIN)
                fd_to_socket[connection.fileno()] = connection
                message_queues[connection] = Queue.Queue()
            # 否则为客户端发送的数据
            else:
                data = sock.recv(1024)
                if data:
                    print "收到数据：", data, "客户端：", sock.getpeername()
                    message_queues[sock].put(data)
                    # 修改读取到消息的连接到等待写事件集合
                    epoll.modify(fd, select.EPOLLOUT)
        # 可写事件
        elif event & select.EPOLLOUT:
            try:
                msg = message_queues[sock].get_nowait()
            except Queue.Empty:
                print sock.getpeername(), " queue empty"
                epoll.modify(fd, select.EPOLLIN)
            else:
                print "发送数据：", data, "客户端：", sock.getpeername()
                sock.send(msg)
        # 关闭事件
        elif event & select.EPOLLHUP:
            epoll.unregister(fd)
            fd_to_socket[fd].close()
            del fd_to_socket[fd]

epoll.unregister(server.fileno())
epoll.close()
server.close()
