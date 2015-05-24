# Example2.py
'''
socket multiThread test
'''

import time
import threading
import Queue
from socket import*


class Consumer(threading.Thread):
    """docstring for Consumer"""
    def __init__(self, queue, host, port):
        self.BUFSIZ = 1024
        self.ADDR = (host, port)
        self.CliSock = socket(AF_INET, SOCK_STREAM)
        threading.Thread.__init__(self, name=host)
        self._queue = queue

    def connect(self):
        try:
            self.CliSock.connect(self.ADDR)
        except Exception, e:
            self.state = 'bad'
            print str(e)

    def run(self):
        self.connect()
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                self.CliSock.close()
                break
            elif isinstance(content, str) and content == 'run':
                if self.state = 'good'
                    try:
                        self.CliSock.send(data)
                        data = self.CliSock.recv(self.BUFSIZ)
                        print self.getName(), data, state
                    except Exception, e:
                        self.state = 'bad'
                else:
                    self.connect()
            else:
                break


def Producer():
    addrs = [('192.168.3.1',5000), ('192.16..3.2', 5001),
            ('192.168.3.3', 5002), ('192.168.3.4', 5004)]
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, addrs)
    start_time = time.time()

    # Add the urls to process
    for url in urls:
        queue.put('run')
    # Add the poison pill
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)


def build_worker_pool(queue, urls):
    workers = []
    for addr in addrs:
        worker = Consumer(queue, addr[0], addr[1])
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    Producer()
