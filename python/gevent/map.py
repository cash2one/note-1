
import time
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import gevent


urls = [
    'http://www.sohu.com',
    'http://www.sina.com',
    'http://sae.sina.com.cn/',
    'http://bj.58.com/',
    'http://www.bootcss.com/',
    'http://xlambda.com/gevent-tutorial/',
    'http://bbs.tianya.cn/',
]

# single thread
start = time.time()
for url in urls:
    ret = urllib2.urlopen(url)
end = time.time()
print end-start
print


# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
start = time.time()
results = pool.map(urllib2.urlopen, urls)
# close the pool and wait for the work to finish
pool.close()
pool.join()
end = time.time()
print end-start
print

from gevent import monkey
monkey.patch_socket()

start = time.time()
threads = [gevent.spawn(urllib2.urlopen, i) for i in urls]
rets = gevent.joinall(threads)
end = time.time()
print end-start
