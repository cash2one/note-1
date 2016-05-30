# -*- coding: utf-8 -*-
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory


HOST = "localhost"
PORT = 5001


class TSClntProtocol(Protocol):
    def sendData(self):
        data = raw_input('>>')
        if data:
            print "...sending %s..." % data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()


class TSClntFactory(ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()