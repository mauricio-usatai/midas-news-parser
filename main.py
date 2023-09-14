from datetime import datetime, timedelta

from src.news import NewsApi
from src.logger import logging

from settings import Settings


settings = Settings()
logger = logging.getLogger(settings.LOGGER)


def main():

    query = settings.NEWS_KEYWORDS
    today = datetime.now()
    yesterday = today - timedelta(days=3)

    news_api = NewsApi()
    response = news_api.get_all(
        query=query,
        date_from=yesterday.strftime("%Y-%m-%d"),
        date_to=today.strftime("%Y-%m-%d"),
    )

    if response:
        articles_urls = news_api.filter_by_keyword(
            keyword=settings.NEWS_KEYWORDS,
            news_api_response=response,
        )


if __name__ == "__main__":
    main()
