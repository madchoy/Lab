from redis import Redis

class RedisClient(object):
    def __init__(self, connection_maker= None):
        if connection_maker is None:
            self.__connection_maker = Redis
        else:
            self.__connection_maker = connection_maker
        self.__connection = None 
        self.__connection = self.__get_connection()

    def __get_connection(self):
        if self.__connection is None:
            self.__connection = self.__connection_maker()
            return self.__connection
        else:
            return self.__connection    
#    
    def set(self, key, value):
        self.__connection.set(key, value)
#        
    def get(self, key):
        return self.__connection.get(key)
#    
    def subscribe(self, channel, callback):
        sub = self.__connection.pubsub()
        sub.subscribe(channel)
        while True:
            for message in  sub.listen():
                if message == 'quit':
                    # this better be from a test
                    return
                callback(message)
                
    def publish(self, channel, message):
        self.__connection.publish(channel, message)
        
if __name__ == "__main__":
    client = RedisClient()
    def callback(message):
        print message
    client.subscribe('achannel', callback )