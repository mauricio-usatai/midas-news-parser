from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    sourceName: str
    author: Optional[str]
    title: Optional[str]
    description: str
    url: str
    publishedAt: str
    content: str
    parsedContent: str = None
