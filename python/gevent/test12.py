# -*- coding: utf-8 -*-
import gevent
from gevent import monkey; monkey.patch_all()
import signal
import zerorpc


class BaseNode(object):
    def __init__(self):
        self._service = None

    @property
    def id(self):
        raise NotImplementedError

    def _create_service(self):
        raise NotImplementedError

    def get_service(self):
        if not self._service:
            self._service = self._create_service()
        return self._service


class RemoteNode(BaseNode):
    def __init__(self, name, host, port):
        super(RemoteNode, self).__init__()
        self.name = name
        self.host = host
        self.port = port

    @property
    def id(self):
        return '%s:%s' % (self.host, self.port)

    def _create_service(self):
        c = zerorpc.Client()
        c.connect('tcp://%s:%s' % (self.host, self.port))
        return c


class LocalNode(BaseNode):
    def __init__(self):
        super(LocalNode, self).__init__()
        self.name = "marmot"

    @property
    def id(self):
        return 'localhost'

    def _create_service(self):
        return LocalService(self)


class LocalService(object):
    def __init__(self, node):
        self.node = node

    def get_base_info(self):
        print 'localservice'


class Marmot(object):
    BIND_HOST = '0.0.0.0'
    PORT = 9001

    @classmethod
    def create_from_cli(cls):
        return cls()

    def __init__(self, *args, **kwargs):
        self.redis = None
        self._nodes = {}

    def _setup_workers(self):
        gevent.spawn_later(10, self._register_agent_worker, 1)

    def _register_agent_worker(self, sleep_interval):
        while True:
            self._register_agent()
            gevent.sleep(sleep_interval)

    def _register_agent(self):
        print '------------------------------'
        print 'done'
        print '------------------------------'

    def _run_rpc(self):
        self.server = zerorpc.Server(LocalService(LocalNode()))
        self.server.bind('tcp://%s:%s' % (self.BIND_HOST, self.PORT))
        self.server.run()

    def run(self):
        self._setup_workers()
        return self._run_rpc()


def main():
    r = Marmot.create_from_cli()
    r.run()


if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.kill)
    main()
