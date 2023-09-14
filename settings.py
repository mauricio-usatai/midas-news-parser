import os
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    """App config"""

    DEPLOY: str = os.environ.get("DEPLOY", "local")

    # AWS config
    AWS_REGION: str = os.environ.get("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID: str = os.environ.get("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY: str = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

    BUCKET: str = os.environ.get("BUCKET", "dev-midas-news-scoring")

    # NewsAPI config
    NEWS_KEYWORDS: str = os.environ.get("NEWS_KEYWORDS")
    NEWS_API_KEY: str = os.environ.get("NEWS_API_KEY", "")

    REQUESTS_TIMEOUT: int = 5  # seconds
    LOGGER: str = "LOGGER"
