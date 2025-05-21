import os

from dotenv import load_dotenv

load_dotenv()

API_PORT = int(os.getenv("API_PORT", "8000"))
API_HOST = os.getenv("API_HOST", "0.0.0.0")
ALLOW_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*")
ALLOW_METHODS = os.getenv("ALLOWED_METHODS", "*")
ALLOW_HEADERS = os.getenv("ALLOWED_HEADERS", "*")
ALLOW_CREDENTIALS = os.getenv("ALLOW_CREDENTIALS", "True")

SERVICE_ROUTES = {
    "/animes": os.getenv("ANIME_SERVICE_URL", "http://localhost:8001"),
    "/user": os.getenv("USER_SERVICE_URL", "http://localhost:8002"),
    "/favorite": os.getenv("FAVORITE_SERVICE_URL", "http://localhost:8003"),
}
