from gevent.pool import Pool

class SocketPool(object):

# why is this example written without a way to start it?  Hopefully the other examples in this tutorial will show an example of this is actually used.
    def __init__(self):
        self.pool = Pool(1000)
        self.pool.start()

    def listen(self, socket):
        while True:
            socket.recv()

    def add_handler(self, socket):
        if self.pool.full():
            raise Exception("At maximum pool size")
        else:
            self.pool.spawn(self.listen, socket)

    def shutdown(self):
        self.pool.kill()

