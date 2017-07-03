import os
import sys

from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

SLEEP_TIME_IN_SECONDS = 5

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://wpdbirrx:je0cRxHuR7ly7nccyAEyKSsyOYpwJyO1@fish.rmq.cloudamqp.com/wpdbirrx"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap_news_dedupe_news_task_queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://friznszh:lvQaHD79bBGldc6eHiQ1KHEC5EaXYgSl@fish.rmq.cloudamqp.com/friznszh"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap_news_scrape_news_task_queue"

scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    text = None

    # Code below is to tested when no articles are imported.
    # if task['source'] == 'cnn':
    #     print 'scraping cnn news'
    #     text = cnn_news_scraper.extract_news(task['url'])
    # else:
    #     print 'News source [%s] is not supported!' % task['source']
    # task['text']=text
    # dedupe_news_queue_client.sendMessage(task)
    
    article = Article(task['url'])
    article.download()
    article.parse()

    task['text']=article.text
    dedupe_news_queue_client.sendMessage(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print e
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)