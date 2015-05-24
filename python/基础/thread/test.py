# -*- coding: utf-8 -*-

import threading
from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop, args = (i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start() #start threads

    for i in nloops:    #wait for all
        threads[i].join() #threads to finish
        #join()--如果你的主线程除了等线程结束外，还有其它事件要做，那么就不用调用join()
        #只有在你要等待线程结束的时候才要调用join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
