#coding=utf-8
import redis

# https://github.com/andymccurdy/redis-py

host = 'localhost'
port = 6379
db = 0

r = redis.StrictRedis(host, port, db)
r.set('foo', 'bar')
r.set('foo', 123)
print(r.get("foo"))

"""
http://zhuhengwei.com/2016/01/27/Redis%E5%AD%98%E5%82%A8%E5%A4%8D%E6%9D%82%E7%B1%BB%E5%9E%8B%E7%9A%84%E6%80%9D%E8%80%83/

　　redis存取复杂类型时，将复杂类型转为json存储有着显著的效率提升和易操作性。把复杂类型转为Json存到redis，取出后再解析成对应的数据类型。
这种方法可解决大部分的对象类型存储问题，适用于redis/memcache等K-V存储系统。

json need to be serialized / deserialized  before save to / after read from redis

"""

