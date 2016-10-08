# -*- coding: utf-8 -*-
import sys
import threading
from socket import *


HOST = 'localhost'
PORT = 61557
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)


def init_UDP():
    try:
        udpCliSock.bind(ADDR)
    except error:
        sys.exit(0)


def recv_data():
    while True:
        data, address = udpCliSock.recvfrom(BUFSIZ)

        if not data:
            break
        if data == 'Exit':
            close_UDP()
            break

        print data, address


def close_UDP():
    print 'DONE'
    udpCliSock.close()


def main():
    init_UDP()
    t = threading.Thread(target=recv_data, args=None)
    t.start()
    t.join()


if __name__ == '__main__':
    main()
