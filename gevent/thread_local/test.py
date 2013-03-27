import gevent
from gevent.local import local

class stuff(object):
	def __init__(self):
		pass

# make instance of stuff to show that the the global variable is accessible by both instances
blah = stuff()
stash = local()

def f1():
    stash.x = 1
    blah.a=1
    print(stash.x)
    print(blah.a)
def f2():
    stash.y = 2
    print(stash.y)
    print(blah.a)
    try:
        stash.x
    except AttributeError:
        print("x is not local to f2")

g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)

gevent.joinall([g1, g2])
