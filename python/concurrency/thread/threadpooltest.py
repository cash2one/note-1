import time
import threading
import Queue
from socket import*


BUFSIZ = 1024


class Consumer(threading.Thread):
    def __init__(self, queue, host, port):
        threading.Thread.__init__(self, name=host)
        self.ADDR = (host, port)
        self.cli_sock = socket(AF_INET, SOCK_STREAM)
        self._queue = queue
        self.state = None

    def connect(self):
        try:
            self.cli_sock.connect(self.ADDR)
        except Exception as e:
            self.state = 'bad'
            print str(e)

    def run(self):
        self.connect()
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                self.cli_sock.close()
                break
            elif isinstance(content, str) and content == 'run':
                if self.state == 'good':
                    try:
                        self.cli_sock.send(data)
                        data = self.cli_sock.recv(BUFSIZ)
                        print self.getName(), data, self.state
                    except Exception as e:
                        self.state = 'bad'
                else:
                    self.connect()
            else:
                break


def producer():
    addrs = [
        ('192.168.3.1', 5000), ('192.16..3.2', 5001),
        ('192.168.3.3', 5002), ('192.168.3.4', 5004)
    ]
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, addrs)
    start_time = time.time()

    # Add the urls to process
    for url in addrs:
        queue.put('run')
    # Add the poison pill
    for worker in worker_threads:
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)


def build_worker_pool(queue, urls):
    workers = []
    for addr in urls:
        worker = Consumer(queue, addr[0], addr[1])
        worker.start()
        workers.append(worker)
    return workers


if __name__ == '__main__':
    producer()
