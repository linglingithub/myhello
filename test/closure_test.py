"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
"""
def count_999():  # this will return all 9s
    fs = []
    for i in [1, 2, 3]:  # still the same as in range(1, 4)
    #for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)  # different f function with reference to i, when execute f1, f2, f3, referencing i as 3
    return fs

def count():  # this will return 1, 4, 9
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f() --> different f(i) with specific i value, when executing f1, f2, f3, with specific i value
    return fs


f1, f2, f3 = count_999()
#f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
# return all 9s instead of 1, 4, 9

