from abc import ABC, abstractmethod
from typing import Optional, List

from datetime import datetime


class News(ABC):
    """
    "Interface" for news apis
    """

    @abstractmethod
    def get_all(
        self,
        query: str,
        date_from: datetime,
        date_to: datetime,
    ) -> Optional[List[dict]]:
        """
        Should return the full response of the api query as
        a list of dicts or None if no articles were found

        Args:
            query (str): The query string to look for
            date_from (datetime): Start date of query
            date_to (datetime): End date of query

        Returns:
            Optional[List[dict]]: A list of dicts describing each article or None
        """
        raise NotImplementedError

    @abstractmethod
    def filter_by_keyword(
        self, keyword: str, news_list: List[dict]
    ) -> Optional[List[str]]:
        """
        Filter a news list by keyword based on the article's
        url, description and title

        Args:
            keyword (str): The keyword to search
            news_list (List[dict]): The news list

        Returns:
            Optional[List[str]]: The filtered list of news
        """
        raise NotImplementedError
