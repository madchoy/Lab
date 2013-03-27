import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)

timer = Timeout(1).start()
thread1 = gevent.spawn(wait)
print timer
try:
    thread1.join(timeout=timer)
except Timeout:
   	print timer
	print('Thread 1 timed out')
