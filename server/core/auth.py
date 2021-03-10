from fastapi import Depends, HTTPException, status
from core import security
from jose import JWTError, jwt
from db import schemas, session
from db.crud import get_user_by_username, create_user
from sqlalchemy.orm import Session


async def get_current_user(
    db: Session = Depends(session.get_db),
    token: str = Depends(security.oauth2_scheme),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, security.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def authenticate_user(
    username: str, password: str, db: Session = Depends(session.get_db)
):
    user = get_user_by_username(db=db, username=username)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


def sign_up_new_user(db, email: str, password: str):
    user = get_user_by_username(db, email)
    if user:
        return False  # User already exists
    new_user = create_user(
        db,
        schemas.UserCreate(
            username=email,
            password=password,
        ),
    )
    return new_user
