from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "SUPER_SECRET"

ALGORITHM = "HS256"


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=12)

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )