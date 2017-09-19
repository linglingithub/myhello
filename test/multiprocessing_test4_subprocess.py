import subprocess
"""
小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。

"""


"""
子进程

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：

"""

def fun_1():
    print('$ nslookup www.python.org')
    print('=====================')
    r = subprocess.call(['nslookup', 'www.python.org'])   # in python use subprocess to run a command
    print('Exit code:', r)

"""

如果子进程还需要输入，则可以通过communicate()方法输入：

上面的代码相当于在命令行执行命令nslookup，然后手动输入：

set q=mx
python.org
exit

"""

def fun_2():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


"""

进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：

"""

def fun_3():
    print("func inside fun_3: ", __name__, fun_3.__name__)
    from multiprocessing import Process, Queue
    import os, time, random

    # 写数据进程执行的代码:
    def write(q):
        print(' >>> Process to write: %s' % os.getpid())
        for value in ['A', 'B', 'C']:
            print(' >>> Put %s to queue...' % value)
            q.put(value)
            time.sleep(random.random())

    # 读数据进程执行的代码:
    def read(q):
        print('<<<< Process to read: %s' % os.getpid())
        while True:
            value = q.get(True)
            print('<<<< Get %s from queue.' % value)

    if __name__ == '__main__':
        print("MAIN inside fun_3: ", __name__)
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=write, args=(q,))
        pr = Process(target=read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()

"""
在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing
需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要
先考虑是不是pickle失败了。

"""

if __name__ == '__main__':
    print("MAIN inside main: ", __name__, "fun_3 name: ", fun_3.__name__)
    # fun_1()
    # fun_2()
    fun_3()