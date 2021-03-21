from fastapi import APIRouter, Depends
from db.schemas import User
from core.auth import get_current_user

users_router = r = APIRouter()


@r.get("/users/me", response_model=User)
async def user_me(current_user=Depends(get_current_user)):
    """Get self user."""
    return current_user
