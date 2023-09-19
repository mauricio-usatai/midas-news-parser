from typing import (
    List,
    Union,
    Optional,
)

import unicodedata
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException

from settings import Settings

from ..logger import logging
from .article import Article
from .news_feed import NewsFeed


settings = Settings()
logger = logging.getLogger(settings.LOGGER)


class NewsApi(NewsFeed):
    def __init__(self, query: str):
        self.api_key = settings.NEWS_API_KEY
        self.query = query

    def get_all(self, date_from: str, date_to: str) -> Optional[dict]:
        """
        Returns the full response of the api query as
        a dict or None if error

        Args:
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
                self.query,
            )
            response = api.get_everything(
                q=self.query,
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
                "q": self.query,
                "from_param": date_from,
                "to": date_to,
            }
        }

        return response

    def filter_by_relevant_content(
        self, raw_news: dict, as_article_list: bool = False
    ) -> Union[List[str], List[Article]]:
        """
        Filter a news list by keyword based on the article's
        url, description and title

        Args:
            raw_news dict: The raw news response
            as_article_list bool: Return the filtered news as a list of articles

        Returns:
            List[str]: The filtered list of news
        """

        # Sort news by most recent first
        sorted_news = sorted(
            raw_news["articles"], key=lambda a: a["publishedAt"], reverse=True
        )

        filtered_news = [
            news
            for news in sorted_news
            if news["title"] is not None
            if (
                self.query in news["url"].lower()
                or self.query in news["description"].lower()
                or self.query in news["title"].lower()
            )
        ]

        if as_article_list:
            return self.generate_article_list(news_list=filtered_news)

        return filtered_news

    def generate_article_list(self, news_list: List[dict]) -> List[Article]:
        """
        Transform a list of raw news (dicts) into a list of Articles

        Args:
            news_list (List[dict]): A news list

        Returns:
            List[Article]: The parsed news as a list of Articles
        """
        articles = []
        for news in news_list:
            author = (
                unicodedata.normalize("NFKD", news["author"])
                if news["author"]
                else None
            )

            articles.append(
                Article(
                    sourceName=unicodedata.normalize("NFKD", news["source"]["name"]),
                    author=author,
                    title=unicodedata.normalize("NFKD", news["title"]),
                    description=unicodedata.normalize("NFKD", news["description"]),
                    url=news["url"],
                    publishedAt=news["publishedAt"],
                    content=unicodedata.normalize("NFKD", news["content"]),
                )
            )

        return articles
