# -*- coding: utf-8 -*-
import time
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool as ProcessPool

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import gevent


urls = [
    'http://www.sohu.com',
    'http://www.sina.com',
    'http://www.qq.com/',
    'http://www.51job.com/',
]

# single thread
st = time.time()
for url in urls:
    ret = urllib2.urlopen(url)
print 'single-thread: %s' % (time.time() - st)
print


# Make the Pool of workers

pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
st = time.time()
results = pool.map(urllib2.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
print 'ThreadPool: %s' % (time.time() - st)
print


# pool = ProcessPool(4)
# st = time.time()
# r = pool.map(urllib2.urlopen, urls)
# pool.close()
# pool.join()
# print 'ProcessPool: %s' % (time.time() - st)
# print


st = time.time()
executor = ThreadPoolExecutor(max_workers=4)
executor.map(urllib2.urlopen, urls)
executor.shutdown()
print 'futures: %s' % (time.time() - st)


from gevent import monkey; monkey.patch_socket()

st = time.time()
threads = [gevent.spawn(urllib2.urlopen, i) for i in urls]
rets = gevent.joinall(threads)
print 'Gevent: %s' % (time.time() - st)
