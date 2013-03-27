import gevent
from gevent import Timeout

seconds = 5

timeout = Timeout(seconds)
timeout.start()

def wait():
    print 'ehhh'
    gevent.sleep(10)


try:
    '''
    
    Greenlet.join(timeout=None)
    Wait until the greenlet finishes or timeout expires. Return None regardless.


    spawn creates the greenlet
    join will trigger it.  Will wait or will timeout.
    '''
    print gevent.spawn(wait).join(timeout=1)
except Timeout:
    print 'Could not complete'
