import jwt
from datetime import datetime, timezone, timedelta
from app.config import CONFIG


payload = {
    "sub": "1",
    "name": "Aniflow User",
    "iat": datetime.now(timezone.utc),
    "exp": datetime.now(timezone.utc) + timedelta(hours=1)
}

token = jwt.encode(payload, CONFIG.JWT_SECRET, algorithm=CONFIG.JWT_ALGORITHM)
print(token)
