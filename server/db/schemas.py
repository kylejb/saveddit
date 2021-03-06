from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    username: str


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Base Properties to receive via API
class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    reddit_refresh_token: str = None
    state: str = None
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
