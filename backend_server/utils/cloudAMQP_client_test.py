from cloudAMQP_client import CloudAMQPClient

CLOUD_AMQP_URL = "amqp://zjxhwhjc:peVUkdg85mRPJPtyG8JxZjktaQ-Q2102@clam.rmq.cloudamqp.com/zjxhwhjc"

TEST_AMQP_NAME = "test"

def test_basic():
	client = CloudAMQPClient(CLOUD_AMQP_URL, TEST_AMQP_NAME)

	sentMsg = {"test": "demo"}
	client.sendMessage(sentMsg)
	client.sleep(10)
	receivedMsg = client.getMessage()
	assert sentMsg == receivedMsg
	print "test_basic passed!"

if __name__ == "__main__":
	test_basic()
