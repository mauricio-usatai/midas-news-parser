import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    """App config"""

    NEWS_API_KEY: str = os.environ.get("NEWS_API_KEY")
