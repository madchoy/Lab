from pub_sub.client.redis_client import RedisClient

class Subscriber(object):
	
	def __init__(self, callback, client = None):
		if client is None:
			self.__client = RedisClient()
		else:
			self.__client = client
		
		self.__callback = callback
		
	def __callback_gevent_wrapper(self):
		pass
	
	def subscribe(self,channel):
		self.__client.subscribe(channel, self.__callback)
		
