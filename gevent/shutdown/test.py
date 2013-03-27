import gevent
import signal

def run_forever():
    print 'running'
    while True:
        print 'i'
        gevent.sleep(1)
    print 'killed' # THIS WONT GET PRINTED WHEN SIQUIT
    
if __name__ == '__main__':
    
    '''
    Some care must be taken if both signals and threads are used in the same program. 
    The fundamental thing to remember in using signals and threads simultaneously is: always perform signal() operations in the main thread of execution. 
    Any thread can perform an alarm(), getsignal(), pause(), setitimer() or getitimer(); 
    only the main thread can set a new signal handler, and the main thread will be the only one to receive signals (this is enforced by the Python signal module, 
    even if the underlying thread implementation supports sending signals to individual threads). 
    This means that signals can’t be used as a means of inter-thread communication. Use locks instead.
    '''
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
    thread = gevent.spawn(run_forever)
    thread.join()
