from typing import Optional, List

from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException

from settings import Settings
from .news import News
from ..logger import logging


settings = Settings()
logger = logging.getLogger(settings.LOGGER)


class NewsApi(News):
    def __init__(self):
        self.api_key = settings.NEWS_API_KEY

    def get_all(
        self, query: str, date_from: str, date_to: str
    ) -> Optional[dict]:
        """
        Returns the full response of the api query as
        a dict or None if error

        Args:
            query (str): The query string to look for
            date_from (str): Start date of query
            date_to (str): End date of query

        Returns:
            Optional[dict]: A dict representing the news api response
        """

        api = NewsApiClient(api_key=self.api_key)

        try:
            logger.info(
                "Querying news api from %s to %s :: query: %s",
                date_from,
                date_to,
                query,
            )
            response = api.get_everything(
                q=query,
                from_param=date_from,
                to=date_to,
            )
        except NewsAPIException as err:
            logger.error(err.get_message())
            return None

        # No articles found on the period
        if len(response["articles"]) == 0:
            return None

        # Add metadata to response
        response["metadata"] = {
            "queryFields": {
                "q": query,
                "from_param": date_from,
                "to": date_to,
            }
        }

        return response

    def filter_by_keyword(
        self, keyword: str, news_api_response: dict
    ) -> Optional[List[str]]:
        """
        Filter a news list by keyword based on the article's
        url, description and title

        Args:
            keyword (str): The keyword to search
            news_api_response dict: The news list

        Returns:
            Optional[List[str]]: The filtered list of news
        """

        # Sort articles by most current first
        articles = sorted(
            news_api_response["articles"], key=lambda a: a["publishedAt"], reverse=True
        )

        articles_urls = [
            article["url"]
            for article in articles
            if (
                keyword in article["url"].lower()
                or keyword in article["description"].lower()
                or keyword in article["title"].lower()
            )
        ]

        return articles_urls
