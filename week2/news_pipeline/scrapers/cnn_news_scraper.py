import os
import random
import requests

from lxml import html

CONFIG_FILE = os.path.join(os.path.dirname(__file__), '..','config_service_client.py')
config = CONFIG_FILE.ConfigService().get("newsPipelineConfig").get("scrapers")

GET_CNN_NEWS_XPATH = config.get("GET_CNN_NEWS_XPATH")

USER_AGENTS_FILE = os.path.join(os.path.dirname(__file__), 'user_agents.txt')
USER_AGENTS =[]

with open(USER_AGENTS_FILE, 'rb') as uaf:
    for ua in uaf.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1])

def getHeaders():
    ua = random.choice(USER_AGENTS)
    headers={
        "Connection": "close",
        "User-Agent": ua
    }

def extract_news(news_url):
    session_requests = requests.session()
    response = session_requests.get(news_url, headers=getHeaders())
    
    news={}

    try:
        tree = html.fromstring(response.content)
        news = tree.xpath(GET_CNN_NEWS_XPATH)
        news = ''.join(news)
    except Exception:
        return{}

    return news