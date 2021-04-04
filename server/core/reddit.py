from uuid import uuid4

import praw
from db.crud import get_user_by_attribute


def reddit_client(token_manager=None):
    return praw.Reddit(
        "saveddit",
        user_agent="obtain_refresh_token_test/v0",
        token_manager=token_manager,
    )


def create_state():
    return str(uuid4())


def create_and_save_state(db, user):
    """Save generated random string for state parameter."""
    user.state = create_state()
    db.commit()
    db.refresh(user)
    return user.state


def is_valid_state(state, db):
    db_user = get_user_by_attribute(db, state=state)
    return db_user


def make_authorization_url(state):
    scopes = ["identity", "history"]

    url = reddit_client().auth.url(scopes, state, "permanent")
    return url


def get_reddit_token(token: str):
    return reddit_client().auth.authorize(token)
