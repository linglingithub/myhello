#coding=utf-8

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


print "=========================="


a = "global a!"


def modify():
    """
    global的使用了是为了在一个代码块中声明一个变量是全局变量。
    在上面这个例子中，modify函数中使用了global，然后修改了a的值，并打印。

在代码最后也打印了a的值。

执行代码输出如下：

global a!
inner a!
inner a!#这里的值被修改了

这说明，global确实起到作用了。

如果这里不使用global的话，那么根据python对变量赋值的原则，这里会在modify这个函数的局部空间中修改变量a，并不会反映到全局。

删除global a之后，再次执行，输出如下：

global a!
inner a!
global a!
    :return: 
    """
    global a   #
    print "inside modify 1: ", a
    a = "inner a!"
    print "inside modify 2: ", a


if __name__ == "__main__":
    print "before modify: ", a
    modify()
    print "after modify: ", a

