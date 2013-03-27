import gevent
from gevent.queue import Queue

class Actor(gevent.Greenlet):

    def __init__(self):
        self.inbox = Queue()
        gevent.Greenlet.__init__(self)

    def receive(self, message):
        """
        Define in your subclass.
        """
        raise NotImplemented()

    def _run(self):
	print 'in run'
        self.running = True

        while self.running:
            print '%s:start run loop'%self.__class__.__name__
            message = self.inbox.get()
            self.receive(message)
            print 'end run loop'
