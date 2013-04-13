import sys
print sys.path
import pub_sub
from pub_sub.client.redis_client import RedisClient
class TestRedisClient(object):
	def test_set_get_live(self):
		client = RedisClient()
		client.set('mkey','blahasdf')
		assert 'blahasdf' == client.get('mkey')

	def test_set(self):
		some_key = 'some_key'
		some_value = 'some_value'
		class MockConnectionMaker(object):
			def set(self, key, value):
				assert some_key == key
				assert some_value == value
				
		client = RedisClient(MockConnectionMaker)
		client.set('some_key','some_value')
		
	
	def test_get(self):
		some_key = 'some_key'
		some_value = 'blahblahblah'
		class MockConnectionMaker(object):
			def get(self, key):
				assert some_key == key 
				return some_value
		client = RedisClient(MockConnectionMaker)
		assert  some_value == client.get('some_key')
		
	def test_subscribe(self):
		
		message_received = 'hello'
		the_channel = 'achannel'
		
		class MockPubSub(object):
			def listen(self):
				return [message_received,'quit']
			
			def subscribe(self, channel):
				assert the_channel == channel
				return MockPubSub()
		
		class MockConnectionMaker(object):
			def pubsub(self):
				return MockPubSub()
			
		def callback(message):
			assert message_received == message
			
		client = RedisClient(MockConnectionMaker)
		client.subscribe(the_channel, callback)
		
	def test_publish(self):
		the_channel = 'channel blah blah'
		message_to_publish = 'yo yo this is a shout out'
		
		class MockConnectionMaker(object):
			def publish(self, channel, message):
				assert the_channel == channel
				assert message_to_publish == message
			
		client = RedisClient(MockConnectionMaker)
		client.publish(the_channel, message_to_publish)
		
		
