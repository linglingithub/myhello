# Python program to illustrate the concept
# of threading
import threading
import os


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    print("Task 1 's main tread: {} --- {}".format(threading.main_thread().name, threading.main_thread().ident))



def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {} -- {}".format(os.getpid(), threading.current_thread().ident))

    # print name of main thread
    print("Main thread name: {}".format(threading.main_thread().name))
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()

"""

http://www.geeksforgeeks.org/multithreading-python-set-1/

Let us try to understand the above code:

We use os.getpid() function to get ID of current process.
print("ID of process running main program: {}".format(os.getpid()))
As it is clear from the output, the process ID remains same for all threads.

We use threading.main_thread() function to get the main thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started. name attribute of thread object is used to get the name of thread.
print("Main thread name: {}".format(threading.main_thread().name))
We use the threading.current_thread() function to get the current thread object.
print("Task 1 assigned to thread: {}".format(threading.current_thread().name))

"""