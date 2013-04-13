from pub_sub.sub import subscriber
import pytest
import tempfile
import os

class TestSubscriber(object):
	def test_subscribe(self):
		channel = 'ufo'
		
		message_received = 'bleh'			
		class MockClient(object):
			def subscribe(self, channel, callback):
				callback(message_received)
				
		def callback(message):
			assert message_received == message
			
		mock_client = MockClient()
		
		subscr = subscriber.Subscriber(callback, client = mock_client)
		subscr.subscribe(channel)


class TestSubscriberLive(object):
	def pytest_funcarg__live(self):
		pytest.config.getvalueorskip('live')
	
#	tmp_file_tuple = namedtuple('tmp_file_tuple', 'tmp_file_path')
#	def pytest_funcarg__tmp_file(self, request):
#		tmpdir = tempfile.gettempdir()
#		path = os.path.join(tmpdir, 'tmpfile')
#		return self.tmp_file_tuple(path)
#		
	def test_live(self, live):
		def print_out(message):
			print message
		subscr = subscriber.Subscriber(print_out)
		subscr.subscribe('achannel')
