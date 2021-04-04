from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from reddit.db_token_manager import DBTokenManager

from db.session import get_db
from db.crud import update_user_refresh_token

from core.auth import get_current_user
from core.reddit import (
    make_authorization_url,
    create_and_save_state,
    is_valid_state,
    get_reddit_token,
    reddit_client,
)

reddit_router = r = APIRouter()


@r.get("/reddit/callback")
def callback(state, code, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate state",
    )

    db_user = is_valid_state(state, db)
    if not db_user:
        raise credentials_exception

    refresh_token = get_reddit_token(code)
    db_user = update_user_refresh_token(db, db_user, refresh_token)

    return RedirectResponse(url="http://localhost:3000")


@r.get("/reddit/authenticate")
async def get_auth_url(
    db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    state = create_and_save_state(db, current_user)
    return make_authorization_url(state)


@r.get("/reddit")
def something(current_user=Depends(get_current_user), db: Session = Depends(get_db)):
    # [TEMP]: Assuming all current_users have refresh tokens here
    TOKEN_MANAGER = DBTokenManager(current_user, db)
    reddit = reddit_client(TOKEN_MANAGER)
    saved_post_list = []
    saved_posts = reddit.user.me().saved(limit=None)
    for post in saved_posts:
        # [TEMP]: Only returns post.id for initial wireframing/scaffolding and testing
        saved_post_list.append(post.id)
    return saved_post_list
