from src.news import NewsApi


def test_news_feed_filter_by_relevant_content(raw_news_feed):
    """
    Test if the raw news filtering is working properly.
    """
    news_feed = NewsApi(query="petrobras")
    filtered_raw_news = news_feed.filter_by_relevant_content(raw_news=raw_news_feed)

    assert len(filtered_raw_news) == 1
    assert len(filtered_raw_news[0]) == 8
    assert filtered_raw_news[0]["title"] == "WEG e Petrobras assinam..."
