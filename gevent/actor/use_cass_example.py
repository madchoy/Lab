from actor import Actor
import gevent
from gevent.queue import Queue
from gevent import Greenlet

class Pinger(Actor):
    def receive(self, message):
        print 'Pinger:%s'% message
        pong.inbox.put('ping')
        gevent.sleep(0)
        print 'pinger out of sleep'

class Ponger(Actor):
    def receive(self, message):
        print 'Ponger:%s'%message
        ping.inbox.put('pong')
        gevent.sleep(0)
        print 'Ponger out of sleep'

ping = Pinger()
pong = Ponger()

print 'about to start'
ping.start()
pong.start()


# comment this out and nothing will happen.  must have a message in ping or pong to start this off
pong.inbox.put('start')

print 'joining all'
gevent.joinall([ping, pong])
