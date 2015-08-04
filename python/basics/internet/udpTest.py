# -*- coding: utf-8 -*-

from socket import *
import sys
import threading
import os

HOST = 'localhost'
PORT = 61557
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

def initUDP():
    try:
        udpCliSock.bind(ADDR)
    except error:
        sys.exit(0)


def RecvData():
    while True:
        data, address = udpCliSock.recvfrom(BUFSIZ)

        if not data:
            break
        if data == 'Exit':
            CloseUDP()
            break

        print data, address

def CloseUDP():
    print 'DONE'
    udpCliSock.close()
    
def main():
    initUDP()
    t = threading.Thread(target = RecvData, args=())
    t.start()
    t.join()
    
if __name__ == '__main__':
    main()
























