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


# ======================= Pipelines

r = redis.Redis()
r.set('bing', 'baz')
# Use the pipeline() method to create a pipeline instance
pipe = r.pipeline()
# The following SET commands are buffered
pipe.set('foo', 'bar')
pipe.get('bing')
# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
tmp = pipe.execute()
print(tmp)
# For ease of use, all commands being buffered into the pipeline return the pipeline object itself. Therefore calls can be chained like:
tmp = pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
# expect [True, True, 6]
print(tmp)
#n addition, pipelines can also ensure the buffered commands are executed atomically as a group. This happens by default.
# If you want to disable the atomic nature of a pipeline but still want to buffer commands, you can turn off transactions.
pipe = r.pipeline(transaction=False)

"""
http://zhuhengwei.com/2016/01/27/Redis%E5%AD%98%E5%82%A8%E5%A4%8D%E6%9D%82%E7%B1%BB%E5%9E%8B%E7%9A%84%E6%80%9D%E8%80%83/

　　redis存取复杂类型时，将复杂类型转为json存储有着显著的效率提升和易操作性。把复杂类型转为Json存到redis，取出后再解析成对应的数据类型。
这种方法可解决大部分的对象类型存储问题，适用于redis/memcache等K-V存储系统。

json need to be serialized / deserialized  before save to / after read from redis

"""

