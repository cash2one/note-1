#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: client.py
# Created: 13/12/2013 09:50:53
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------


from socket import*

class TcpClient():

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)

    def connect(self):
        print self.ADDR
        self.tcpCliSock.connect(self.ADDR)

    def sendData(self, data):
        if data:
            self.tcpCliSock.send(data)
        else:
            pass

    def recvData(self):
        data = self.tcpCliSock.recv(self.BUFSIZ)
        return data

    def close(self):
        self.tcpCliSock.close()
    
