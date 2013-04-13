from pub_sub.client.redis_client import RedisClient
class Publisher(object):
    def __init__(self, client=None):
        if client is not None:
            self.__client = client
        else:
            self.__client = RedisClient()
            
    def publish(self, channel, message):
        self.__client.publish(channel, message)
        
