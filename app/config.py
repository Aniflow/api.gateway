import os

from dotenv import load_dotenv

load_dotenv()

ANIME_SERVICE_URL = os.getenv("ANIME_SERVICE_URL", "http://127.0.0.1:8001")
API_PORT = int(os.getenv("API_PORT", "8000"))
API_HOST = os.getenv("API_HOST", "0.0.0.0")
