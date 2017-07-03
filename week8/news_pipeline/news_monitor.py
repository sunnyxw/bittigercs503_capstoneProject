import datetime
import hashlib
import os
import redis
import sys


#import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloudAMQP_client import CloudAMQPClient

NEWS_SOURCES =[
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]

REDIS_HOST ="localhost"
REDIS_PORT=6379

# set timeout as 0.5 hrs. Chan set it as 24 hrs.
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 1
SLEEP_TIME_IN_SECONDS=10

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://friznszh:lvQaHD79bBGldc6eHiQ1KHEC5EaXYgSl@fish.rmq.cloudamqp.com/friznszh"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap_news_scrape_news_task_queue"
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    num_of_new_news =0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')

        if redis_client.get(news_digest) is None:
            num_of_new_news = num_of_new_news +1
            news['digest'] = news_digest

            #if no publish data available, set it as current UTC time
            if news['publishedAt'] is None:
                # make the time in format yyyy-mm-ddthh:mm:ss in UTC
                news['publishedAt'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

            redis_client.set(news_digest, news)
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

            cloudAMQP_client.sendMessage(news)

    print "Fetched %d news." % num_of_new_news

    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)