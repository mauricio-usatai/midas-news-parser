import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    """App config"""
    DEPLOY: str = os.environ.get("DEPLOY", "local")

    NEWS_KEYWORDS: str = os.environ.get("NEWS_KEYWORDS")
    NEWS_API_KEY: str = os.environ.get("NEWS_API_KEY", "")

    LOGGER: str = "LOGGER"
