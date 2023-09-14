from typing import Optional

import json
from io import StringIO
from datetime import datetime, timedelta

import pandas as pd
import requests
from requests.exceptions import RequestException

from src.object_storage import S3ObjectStorage
from src.source_page_parser import SourcePageParser
from src.news import (
    NewsApi,
    NewsFeed,
)
from src.logger import logging
from settings import Settings


settings = Settings()
logger = logging.getLogger(settings.LOGGER)


def get_news(news_feed: NewsFeed) -> Optional[dict]:
    today = datetime.now()
    yesterday = today - timedelta(days=1)

    response = news_feed.get_all(
        date_from=yesterday.strftime("%Y-%m-%dT00:00:00"),
        date_to=today.strftime("%Y-%m-%d"),
    )

    return response


def get_page_source(url: str) -> Optional[str]:
    try:
        response = requests.get(url, timeout=settings.REQUESTS_TIMEOUT)
    except RequestException as err:
        logger.error(err)
        return None

    if response.status_code != 200:
        return None

    return response.text


def main():
    date = datetime.now().isoformat(timespec="seconds")

    news_feed: NewsFeed = NewsApi(query=settings.NEWS_KEYWORDS)
    raw_news = get_news(news_feed=news_feed)

    if not raw_news:
        logger.info("No news avaiable at this time")
        return

    # Save raw news_feed to object storage
    buffer = StringIO()
    json.dump(raw_news, buffer)
    S3ObjectStorage().put(
        path=f"news-feed-responses/{date}-news-feed.json",
        bucket=settings.BUCKET,
        body=buffer,
    )

    articles = news_feed.filter_by_relevant_content(
        raw_news=raw_news,
        as_article_list=True,
    )

    for article in articles:
        page_source = get_page_source(article.url)
        if page_source:
            article.parsedContent = SourcePageParser.parse(page_source)

    articles_df = pd.DataFrame([article.model_dump() for article in articles])

    # Save raw news_feed to object storage
    buffer = StringIO()
    articles_df.to_csv(buffer)
    S3ObjectStorage().put(
        path=f"news-feed-articles/{date}-articles.csv",
        bucket=settings.BUCKET,
        body=buffer,
    )


if __name__ == "__main__":
    main()
