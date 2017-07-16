import datetime
import hashlib
import os
import redis
import sys

from config_service_client import ConfigService


#import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client
from cloudAMQP_client import CloudAMQPClient

config = ConfigService().newsPipelineConfig().get("news_monitor")


NEWS_SOURCES = config.get("NEWS_SOURCES")

REDIS_HOST =config.get("REDIS_HOST")
REDIS_PORT=config.get("REDIS_PORT")

# set timeout as 0.5 hrs. Chan set it as 24 hrs.
NEWS_TIME_OUT_IN_SECONDS = config.get("NEWS_TIME_OUT_IN_SECONDS")
SLEEP_TIME_IN_SECONDS=config.get("SLEEP_TIME_IN_SECONDS")

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)

SCRAPE_NEWS_TASK_QUEUE_URL = config.get("SCRAPE_NEWS_TASK_QUEUE_URL")
SCRAPE_NEWS_TASK_QUEUE_NAME = config.get("SCRAPE_NEWS_TASK_QUEUE_NAME")
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