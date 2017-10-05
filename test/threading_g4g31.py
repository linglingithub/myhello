import threading

# global variable x
#x = 0


def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1


def thread_task():
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        increment()


def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))

"""

http://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/

In above program:

Two threads t1 and t2 are created in main_task function and global variable x is set to 0.
Each thread has a target function thread_task in which increment function is called 100000 times.
increment function will increment the global variable x by 1 in each call.
The expected final value of x is 200000 but what we get in 10 iterations of main_task function is some different values.

This happens due to concurrent access of threads to the shared variable x. This unpredictability in value of x is 
nothing but race condition.

Hence, we need a tool for proper synchronization between multiple threads.

Using Locks

threading module provides a Lock class to deal with the race conditions. Lock is implemented using a Semaphore object provided by the Operating System.

A semaphore is a synchronization object that controls access by multiple processes/threads to a common resource in a parallel programming environment. It is simply a value in a designated place in operating system (or kernel) storage that each process/thread can check and then change. Depending on the value that is found, the process/thread can use the resource or will find that it is already in use and must wait for some period before trying again. Semaphores can be binary (0 or 1) or can have additional values. Typically, a process/thread using semaphores checks the value and then, if it using the resource, changes the value to reflect this so that subsequent semaphore users will know to wait.
Lock class provides following methods:

acquire([blocking]) : To acquire a lock. A lock can be blocking or non-blocking.
When invoked with the blocking argument set to True (the default), thread execution is blocked until the lock is unlocked, then lock is set to locked and return True.
When invoked with the blocking argument set to False, thread execution is not blocked. If lock is unlocked, then set it to locked and return True else return False immediately.
release() : To release a lock.
When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.
If lock is already unlocked, a ThreadError is raised.


"""

