import news_api_client as client 

def test_basic():
    news = client.getNewsFromSource()
    print news
    assert len(news) > 0
    print "cnn news successfully loaded!"

    news = client.getNewsFromSource(sources=['bbc-news'])
    print news
    assert len(news) > 0
    print "bbc-news successfully loaded!"

if __name__ == "__main__":
    test_basic()

