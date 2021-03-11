import json
import os

from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


with open(os.path.join("secrets.json")) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        raise KeyError("Improperly Configured")


SECRET_KEY = get_secret("SECRET_KEY")
ALGORITHM = get_secret("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = get_secret("ACCESS_TOKEN_EXPIRE_MINUTES")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
