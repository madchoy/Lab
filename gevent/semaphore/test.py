from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore(2)
'''
note: The difference between the number of times and a semaphore has been acquired and released is called the bound of the semaphore. If a semaphore bound reaches 0 it will block until another greenlet releases its acquisition.
A semaphore with bound of 1 is known as a Lock. it provides exclusive execution to one greenlet. They are often used to ensure that resources are only in use at one time in the context of a program.
'''

def worker1(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)

def worker2(n):
    with sem:
        print('Worker %i acquired semaphore' % n)
        sleep(0)
    print('Worker %i released semaphore' % n)

pool = Pool()
pool.map(worker1, xrange(0,2))
pool.map(worker2, xrange(3,6))
