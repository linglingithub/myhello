"""
with some_lock:
# do something...
is equivalent
to:

some_lock.acquire()
try:
# do something...
finally:
    some_lock.release()

Locks
implement
the
context
manager
API and are
compatible
with the with statement.By using locks in the with statement, we do not need to explicitly acquire and release the lock:
"""

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s', )


def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_not_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    w = threading.Thread(target=worker_with, args=(lock,))
    nw = threading.Thread(target=worker_not_with, args=(lock,))

    w.start()
    nw.start()
