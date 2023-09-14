from abc import ABC, abstractmethod
from typing import Optional, List


class NewsFeed(ABC):
    """
    "Interface" for news apis
    """

    @abstractmethod
    def get_all(
        self,
        date_from: str,
        date_to: str,
    ) -> Optional[dict]:
        """
        Should return the full response of the api query as
        a dict or None if error

        Args:
            date_from (str): Start date of query
            date_to (str): End date of query

        Returns:
            Optional[dict]: A dict representing the news api response
        """
        raise NotImplementedError

    @abstractmethod
    def filter_by_relevant_content(self, raw_news: dict) -> List[str]:
        """
        Filter a news list by keyword based on the article's
        url, description and title

        Args:
            raw_news dict: The raw news response

        Returns:
            [List[str]: The filtered list of news
        """
        raise NotImplementedError
