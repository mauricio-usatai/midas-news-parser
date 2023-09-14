import re
import unicodedata

from bs4 import BeautifulSoup


class SourcePageParser:
    @staticmethod
    def parse(page_source: str) -> str:
        """
        Parses an HTML page source to extract only text in <p>
        elements

        Args:
            page_source (str): The HTML source

        Returns:
            str: The text found in <p> elements in the source
        """

        soup = BeautifulSoup(page_source, "html.parser")
        _ = [element.extract() for element in soup.find_all(["script", "style"])]
        p_soup = soup.find_all("p")

        text = [elements.text for elements in p_soup]
        text = "\n".join(text)
        text = re.sub(r"\n+", "\n", text)
        text = re.sub(r"\s\n\s+", "\n", text)
        text = unicodedata.normalize("NFKD", text)

        return text
