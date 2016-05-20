# -*- coding: utf-8 -*-
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)


class RedisQueue(object):
    """Simple Queue with Redis Backend"""
    def __init__(self, name, size=256, namespace='queue', host='localhost', port=6379, db=0):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self._db = redis.StrictRedis(host=host, port=port, db=db)
        self.key = '%s:%s' % (namespace, name)
        self._qsize = size

    def length(self):
        """Return the approximate size of the queue."""
        return self._db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.length() == 0

    def put(self, item):
        """Put item into the queue."""
        if self.length() >= self._qsize:
            self._db.ltrim(self.key, 0, (self._qsize - 2))
        return self._db.rpush(self.key, item)

    def pre_all(self):
        return r.lrange(self.key, 0, -1)

    def pop_all(self):
        return [self._db.lpop(self.key) for i in xrange(self.length())]

    def get(self, block=False, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self._db.blpop(self.key, timeout=timeout)
        else:
            item = self._db.lpop(self.key)

        if item:
            item = item[1]
        return item


class RedisLogger(object):
    def __init__(self, name, size=256, namespace='log'):
        self._db = redis.StrictRedis(host='localhost', port=6379, db=0)
        self._qsize = size
        self.key = '%s:%s' % (namespace, name)
        self._db.rpush(self.key, '*'*15+'Marmot'+'*'*15)
        self._db.expire(self.key, 60*5)

    def length(self):
        return self._db.llen(self.key)

    def put(self, item):
        if self.length() >= self._qsize:
            print self.length()
            self._db.ltrim(self.key, 0, (self._qsize - 2))
        return self._db.rpush(self.key, item)

    def pre_all(self):
        return r.lrange(self.key, 0, -1)

    def pop_all(self):
        return [self._db.lpop(self.key) for i in xrange(self.length())]

    def pop(self, block=False, timeout=None):
        if block:
            item = self._db.blpop(self.key, timeout=timeout)
        else:
            item = self._db.lpop(self.key)

        if item:
            item = item[1]
        return item


logger = RedisLogger('test')


for i in xrange(300):
    logger.put(str(i))


print logger.pre_all()

print

print logger.pop_all()

print logger.pop_all()


print logger.pop()

# print r.info()
# print r.setnx('set', 100)
# print r.set('foo1', 'bar')
# print r.set('foo2', 'bar')

# print json.loads(r.get('172.16.10.152'))

# print r.mget(['foo1', 'foo2', 'foo'])
# print r.mget(['foo1', 'foo2', 'foo'])


# print r.set("number", 3)
# print r.get('list')
# print r.incr("number", 5)
# print r.decr("number", 2)

# print r.delete('list')


# print r.rpush("list", "abc")
# print r.rpush("list", "def")
# print r.rpush("list", "ghi")
# print r.rpush("list", "jkl")
# print r.rpush("list", "mno")
#
# # print r.lrange("list", 0, -1)
# print r.ltrim('list', 0, 2)
#
# print r.lpop('list')
# print r.lpop('list')
# print r.lpop('list')
# print r.lpop('list')
# print r.lpop('list')


# print r.lpush("list", "111")
# print r.lpush("list", "222")
# print r.lpush("list", "333")

# r.expire('list', 10)

# print r.lrange("list", 0, 2)

# print r.lrange("list", 0, -1)
#
# # print r.lrem('list', 1, 'one')  # 删除1个值为"one"的元素
#
# print r.lpop('list')
# print r.rpop('list')  # 移除并获取列表最后一个元素

# print r.delete('list')

# print r.rpop('list')
# print r.lpop('list')

# print r.getset('list')

# print r.llen("list")


# print r.sadd('set', True)
# print r.sadd('set', 222)
# print r.smembers('set')

# print r.spop('set')
# print r.srem('set', 12)
# print r.sinter('set')
# print r.sunion()
# print r.sdiff()

# print r.scard('set')


# print r.dbsize()

print r.keys()

# print r.type('set')
# r.rename("list", 'w')
# r.exists('key')
# r.delete('key')
# r.flushdb()


print r.dbsize()  # 库里有多少key, 多少条数据

# r.save()  # 强行把数据库保存到硬盘。保存时阻塞

# r.flushdb()  # 删除当前数据库的所有数据

# a = r.get('chang')  # a是None

# r.exists('chang')  # 看是否存在这个键值

# r.keys()   # 列出所有键值