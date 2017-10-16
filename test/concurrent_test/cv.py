import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def consumer(cv):
    logging.debug('Consumer thread started ...')
    with cv:
        logging.debug('Consumer waiting ...')
        cv.wait()
        logging.debug('Consumer and get lock again consumed the resource')
        logging.debug('Consumer {} is going to release the lock'.format(threading.current_thread()))

def producer(cv):
    logging.debug('Producer thread started ...')
    with cv:
        logging.debug('Producer get the lock , Making resource available')
        logging.debug('Notifying to all consumers')
        cv.notifyAll()
        logging.debug('Producer is going to release the lock')



"""

with some_lock:
    # do something...
is equivalent to:

some_lock.acquire()
try:
    # do something...
finally:
    some_lock.release()
"""

def main():
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1', target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2', target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()

if __name__ == '__main__':
    main()

"""

Note that we did not use acquire() and release() methods at all since we utilized the lock object's context manager function (Using locks in the with statement - context manager). Instead, our threads used with to acquire the lock associated with the Condition.

The wait() method releases the lock, and then blocks until another thread awakens it by calling notify() or notify_all().

Note that the notify() and notify_all() methods don't release the lock; this means that the thread or threads awakened will not return from their wait() call immediately, but only when the thread that called notify() or notify_all() finally relinquishes ownership of the lock.

The typical programming style using condition variables uses the lock to synchronize access to some shared state; threads that are interested in a particular change of state call wait() repeatedly until they see the desired state, while threads that modify the state call notify() or notify_all() when they change the state in such a way that it could possibly be a desired state for one of the waiters.



"""