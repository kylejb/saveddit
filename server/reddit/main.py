import random
import sys

import praw

from .db_token_manager import DBTokenManager


def main(state):
    """Provide the program's entry point when directly executed."""
    scopes = ["identity", "history"]

    reddit = praw.Reddit(
        redirect_uri="http://localhost:8000/auth",
        user_agent="obtain_refresh_token_test/v0",
    )

    url = reddit.auth.url(scopes, state, "permanent")
    print(f"Now open this url in your browser: {url}")
    return reddit


def reddit_auth(reddit, token):
    return reddit.auth.authorize(token)


def state_generator():
    return str(random.randint(0, 65000))


###
def initialize_refresh_token_file():
    # this should check if user has a token
    pass


def main_():
    initialize_refresh_token_file()

    #! must pass current user's token here
    refresh_token_manager = DBTokenManager()
    reddit = praw.Reddit(
        "saveddit",
        token_manager=refresh_token_manager,
        user_agent="use_file_token_manager_test/v0",
    )

    scopes = reddit.auth.scopes()
    if scopes == {"*"}:
        print(f"{reddit.user.me()} is authenticated with all scopes")
    elif "identity" in scopes:
        print(
            f"{reddit.user.me()} is authenticated with the following scopes: {scopes}"
        )
    else:
        print(f"You are authenticated with the following scopes: {scopes}")


if __name__ == "__main__":
    sys.exit(main())
