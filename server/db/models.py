from sqlalchemy import Column, Integer, String

from .session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    state = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    reddit_refresh_token = Column(String)
