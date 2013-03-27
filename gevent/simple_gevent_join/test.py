import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

def bleh():
    print('BLEH')
    gevent.sleep(5)
    print('out of BLEH')
gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    gevent.spawn(bleh),
])
