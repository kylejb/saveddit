from fastapi import APIRouter, Depends, Request
from db.crud import create_user
from db.schemas import UserCreate, User
from db.session import get_db
from core.auth import get_current_user

users_router = r = APIRouter()


@r.get("/users/me", response_model=User)
async def user_me(current_user=Depends(get_current_user)):
    """Get self user."""
    return current_user


@r.post("/users", response_model=User)
async def user_create(
    request: Request,
    user: UserCreate,
    db=Depends(get_db),
):
    """Create a new user."""
    return create_user(db, user)
