import gevent
from gevent import Greenlet
import signal

class MyGreenlet(Greenlet):

    def __init__(self, message, n):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)

    def _shutdown(self):
        print 'killed'

if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.shutdown)
#    thread = gevent.spawn(run_forever)
#    thread.join()

    g = MyGreenlet("Hi there!", 3)
    g.start()
    g.join()
