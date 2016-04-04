# -*- coding: utf-8 -*-
from time import ctime
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


PORT = 5001


class TSServerProtocol(Protocol):
    def connectionMade(self):
        client = self.client = self.transport.getPeer().host
        print 'Got connection from', client

    def connectionLost(self, reason):
        print self.transport, 'disconnected'

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))


factory = Factory()
factory.protocol = TSServerProtocol

print 'waiting for connection...'

reactor.listenTCP(PORT, factory)
reactor.run()
