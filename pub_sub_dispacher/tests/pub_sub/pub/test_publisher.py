from pub_sub.pub.publisher import Publisher
import pytest
class TestPublisher(object):
    def test_publish(self):
        the_message = 'bleh'
        the_channel = 'channel'
        class MockClient(object):
            def publish(self, channel, message):
                assert the_channel == channel
                assert the_message == message
        mock_client = MockClient()
        publisher = Publisher(client=mock_client)
        publisher.publish(the_channel, the_message)
        
class TestPublisherLive(object):
    def pytest_funcarg__live(self, request):
        pytest.config.getvalueorskip('live')
    
    def test_live(self, live):
        publisher = Publisher()
        publisher.publish('achannel','hi')
