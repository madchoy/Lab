import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)

def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1) # decrements queue size by 1
            print('Worker %s got task %s' % (n, task))
            timeout_dic = {'steve':1,
                           'john':2,
                           'bob':4}
            timeout = timeout_dic[n]
            gevent.sleep(timeout)
    except Empty:
        print('Quitting time!')

def boss():
    """
    Boss will wait to hand out work until a individual worker is
    free since the maxsize of the task queue is 3.
    """

    for i in xrange(1,10):
        tasks.put(i)
    print('Assigned all work in iteration 1')

    for i in xrange(10,30):
        tasks.put(i) # can only put into queue if there is room to put.  max is 3.  have to wait for something on the queue to free up.
        # when a greenlet gets from the queue, the queue has a space open up.  which allows another operation to be put onto the queue.
        #  the greenlet will stop get from the queue once there is nothing left to consume on the queue. 
    print('Assigned all work in iteration 2')

gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
])
