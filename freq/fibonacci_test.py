def fibo(n):
    """
    create a generator by use yield
    :param n: 
    :return: 
    """
    a, b = 0, 1
    cnt = 0
    while cnt < n:
        yield a
        a, b = b, a+b
        cnt += 1


def fibo_list(n):
    a, b = 0, 1
    res = []
    cnt = 0
    while cnt < n:
        res.append(a)
        a, b = b, a+b
        cnt += 1
    return res

def fibo_recur(n):
    def helper(cnt, a, b):
        if cnt >= n:
            return a
        return helper(cnt+1, b, a+b)

    return helper(1, 0, 1)   # should be 1,0,1 here, not 0, 0 , 1

def fibo_recur2(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo_recur2(n-1) + fibo_recur2(n-2)

n = 10
for i in fibo(n):
    print(i, " ")
fg = fibo(n)
print("==== fibo genenerator: ", fg)
# tmp = fg.next()
# while tmp:
#     print(tmp)
#     tmp = fg.next()

a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
f.next()
f.next()
f.next()
f.next()
print f.next()


for i in fibo_list(n):
    print(i, " ")

print("==== ", len(fibo_list(n)))

print("==== recur: ", fibo_recur(n))
print("==== recur2: ", fibo_recur2(n))