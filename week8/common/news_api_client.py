import requests

from json import loads

# API key is for private use. Please don't abuse. thanks! :)
NEWS_API_KEY ="eaa002d92d8c41b3aa1f7f904dff7fe8"
NEWS_API_ENDPOINT="https://newsapi.org/v1/"
ARTICLES_API="articles"

BBC = 'bbc'
CNN= 'cnn'
DEFAULT_SOURCES = [CNN]

SORT_BY_TOP='top'

def buildUrl(end_point=NEWS_API_ENDPOINT, api_name=ARTICLES_API):
    return end_point + api_name

def getNewsFromSource(sources=[DEFAULT_SOURCES], sortBy=SORT_BY_TOP):
    articles =[]
    for source in sources:
        payload ={ 'apiKey': NEWS_API_KEY,
                    'source': source,
                    'sortBy': sortBy
        }
        response = requests.get(buildUrl(), params=payload)
        res_json = loads(response.content)

        # extract news from response
        if (res_json is not None and 
            res_json['status'] == 'ok' and 
            res_json['source'] is not None):
            # populate news source in each article
            for news in res_json['articles']:
                news['source']=res_json['source']

            articles.extend(res_json['articles'])

    return articles