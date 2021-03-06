from sqlalchemy.orm import Session
from . import models, schemas
import bcrypt


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_attribute(db: Session, **filter_attributes):
    query = db.query(models.User)
    for attr, value in filter_attributes.items():
        query = query.filter(getattr(models.User, attr) == value)
    results = query.first()
    return results


def create_user(db: Session, user: schemas.UserCreate):
    hashing_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    db_user = models.User(username=user.username, hashed_password=hashing_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_refresh_token(db: Session, db_user, reddit_refresh_token: str):
    db_user.reddit_refresh_token = reddit_refresh_token
    db.commit()
    db.refresh(db_user)
    return db_user
