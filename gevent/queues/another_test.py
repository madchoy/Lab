import gevent
from gevent.queue import JoinableQueue

def worker():
    while True:
        item = q.get()
        try:
            do_work(item)
        finally:
            q.task_done()

num_worker_threads = 3
q = JoinableQueue()
for i in range(num_worker_threads):
     gevent.spawn(worker)

for item in source():
    q.put(item)

q.join()  # block until all tasks are done
