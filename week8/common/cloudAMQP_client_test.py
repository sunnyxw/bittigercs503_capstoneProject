from cloudAMQP_client import CloudAMQPClient

# CLOUDAMQP_URL = 'amqp://kigqrfvc:WvC0LqofQpQ7GM_xPO1drlbOEn0E-6lO@fish.rmq.cloudamqp.com/kigqrfvc'
# QUEUE_NAME = 'test'

CLOUDAMQP_URL='amqp://friznszh:lvQaHD79bBGldc6eHiQ1KHEC5EaXYgSl@fish.rmq.cloudamqp.com/friznszh'
QUEUE_NAME ='tap_news_scrape_news_task_queue'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

    sentMsg = {'test_key':'test_value'}
    client.sendMessage(sentMsg)
    client.sleep(5)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print 'test_basic passed.'

if __name__ == "__main__":
    test_basic()
