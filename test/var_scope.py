__author__ = 'linglin'

def test_var_scope(x):
    print "x = ", x
    x = "in method value"
    print "x = ", x
    if True:
        x = "in true value"
        print "x = ", x
    print "after true: x = ", x

def test_var_scope1(x):
    print "x = ", x
    x = ["in method value"]
    print "x = ", x
    if True:
        x = ["in true value"]
        print "x = ", x
    print "after true: x = ", x

def test_var_scope2(x):
    print "x = ", x
    x[0] = "in method value"
    print "x = ", x
    if True:
        x[0] = "in true value"
        print "x = ", x
    print "after true: x = ", x


a = [3] # 3
test_var_scope2(a)
print "after method: a = ", a