from abc import ABC, abstractmethod
from typing import Optional, List


class News(ABC):
    """
    "Interface" for news apis
    """

    @abstractmethod
    def get_all(
        self,
        query: str,
        date_from: str,
        date_to: str,
    ) -> Optional[dict]:
        """
        Should return the full response of the api query as
        a dict or None if error

        Args:
            query (str): The query string to look for
            date_from (str): Start date of query
            date_to (str): End date of query

        Returns:
            Optional[dict]: A dict representing the news api response
        """
        raise NotImplementedError

    @abstractmethod
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
        raise NotImplementedError
