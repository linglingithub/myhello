def consumer():
    n = 0
    print("consumer init")
    while True:
        n = yield n
        if not n:
            raise Exception('no production')
        n -= 1
        print("consuption 1,left %d" % n)
def produce(c):
    n = 0
    next(c)
    while n < 6:
        n +=2
        print("produce 2,left %d" % n)
        n = c.send(n)
        print("left %d" % n)
    c.close()
c = consumer()
produce(c)