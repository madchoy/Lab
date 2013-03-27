import gevent
from gevent.queue import Queue

tasks = Queue()


def boss():
    for i in xrange(1,25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

