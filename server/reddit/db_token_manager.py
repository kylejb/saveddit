from praw.util.token_manager import BaseTokenManager
from db import crud
from db.session import get_db


class DBTokenManager(BaseTokenManager):
    """Wrapper to interact with BaseTokenManager (an Abstract Class)."""

    def __init__(self, current_user):
        """Load and save refresh token from user attribute.

        :param current_user_token: The string value of user's refresh token
        """
        super().__init__()
        self._current_user = current_user
        self._current_user_token = current_user.reddit_refresh_token

    def post_refresh_callback(self, authorizer):
        """Update the saved copy of the refresh token.

        Handle callback that is invoked after a refresh token is used.
        :param authorizer: The ``prawcore.Authorizer`` instance used containing

        ``access_token`` and ``refresh_token`` attributes.
        This function will be called after refreshing the access and refresh
        tokens. This callback can be used for saving the updated
        ``refresh_token``.
        """
        # TODO - Refactor persistence to DB logic.
        # self._current_user.reddit_refresh_token = authorizer.refresh_token
        self._helper(get_db(), self._current_user.id)

    def pre_refresh_callback(self, authorizer):
        """Load the refresh token from user.

        Handle callback that is invoked before refreshing PRAW's authorization.

        :param authorizer: The ``prawcore.Authorizer`` instance used containing

        ``access_token`` and ``refresh_token`` attributes.
        This callback can be used to inspect and modify the attributes of the
        ``prawcore.Authorizer`` instance, such as setting the
        ``refresh_token``.
        """
        authorizer.refresh_token = self._current_user_refresh_token

    def _helper(db, user_id, authorizer):
        db_user = crud.get_user(db=db, user_id=user_id)
        db_user.reddit_refresh_token = authorizer.refresh_token
        db.commit()
        db.refresh(db_user)
        return db_user
