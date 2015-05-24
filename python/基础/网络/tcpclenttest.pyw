#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File: tcpclenttest.py
# Created: 13/12/2013 10:21:24
# Author: baixue
# Purpose:
#-------------------------------------------------------------------------------

from PyQt4 import QtGui, QtCore
import tcpclient

class Client(QtGui.QWidget):

    def __init__(self):
        super(Client, self).__init__()

        self.addrLabel = QtGui.QLabel(u'地址')
        self.addr = QtGui.QLineEdit()
        self.portLabel = QtGui.QLabel(u'端口')
        self.port = QtGui.QSpinBox()
        self.port.setRange(0,65535)
        self.dataText = QtGui.QTextBrowser()
        self.conn = QtGui.QPushButton('Connect')
        self.conn.clicked.connect(self.connect)
        self.send = QtGui.QPushButton('Send')
        self.send.clicked.connect(self.start)
        self.close = QtGui.QPushButton('Disconnect')
        self.close.clicked.connect(self.disconnect)

        vLayout = QtGui.QVBoxLayout()
        vLayout.addWidget(self.addrLabel)
        vLayout.addWidget(self.addr)
        vLayout.addWidget(self.portLabel)
        vLayout.addWidget(self.port)
        vLayout.addWidget(self.dataText)

        hLayout = QtGui.QHBoxLayout()
        hLayout.addWidget(self.conn)
        hLayout.addWidget(self.send)
        hLayout.addWidget(self.close)

        layout = QtGui.QVBoxLayout()
        layout.addLayout(vLayout)
        layout.addLayout(hLayout)
        
        self.setLayout(layout)
        self.setWindowTitle("TCPClientTest")

        self.addr.setText('166.111.89.174')
        self.port.setValue(12001)

        self.timerID = 0

    def connect(self):
        host = str(self.addr.text())
        port = self.port.value()
        self.TcpClient = tcpclient.TcpClient(host, port)
        self.TcpClient.connect()

    def start(self):
        self.timerID = self.startTimer(1000)

    def disconnect(self):
        self.killTimer(self.timerID)
        self.TcpClient.close()

    def timerEvent(self, e):
        '定时器触发事件'
        self.TcpClient.sendData('ashdata')
        data = self.TcpClient.recvData()
        data = data.split('@',data.count('@'))
        #要将data按gb2312解码，不然中文会乱码
        self.dataText.append(data[2])
        



















if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    client = Client()
    client.show()
    sys.exit(app.exec_())
