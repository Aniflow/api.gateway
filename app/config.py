import os

from dotenv import load_dotenv

load_dotenv()


SERVICE_ROUTES = {
    "/animes": os.getenv("ANIME_SERVICE_URL", "http://localhost:8001"),
    "/user": os.getenv("USER_SERVICE_URL", "http://localhost:8002"),
    "/favorite": os.getenv("FAVORITE_SERVICE_URL", "http://localhost:8003"),
}


class BaseConfig:
    """Base configuration with common settings."""
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    ALLOW_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    ALLOW_METHODS: str = os.getenv("ALLOWED_METHODS", "*")
    ALLOW_HEADERS: str = os.getenv("ALLOWED_HEADERS", "*")
    ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "True").lower() in ("true", "1")  # Noqa: E501
    JWT_SECRET: str = os.getenv("JWT_SECRET", "your-dev-secret")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")


class DevelopmentConfig(BaseConfig):
    """Configuration for development."""
    DEBUG: bool = True


class ProductionConfig(BaseConfig):
    """Configuration for production."""
    DEBUG: bool = False


ENV = os.getenv("ENV", "development").lower()
CONFIG = DevelopmentConfig() if ENV == "development" else ProductionConfig()
