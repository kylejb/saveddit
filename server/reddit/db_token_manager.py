from praw.util.token_manager import BaseTokenManager


class DBTokenManager(BaseTokenManager):
    """Wrapper to interact with an Abstract Class."""

    def __init__(self, current_user, db):
        """Load and save refresh token from current_user.

        :param current_user: Instance of current_user object
        :param db: Current session of db
        """
        super().__init__()
        self._db = db
        self._current_user = current_user
        self._current_user_refresh_token = current_user.reddit_refresh_token

    def post_refresh_callback(self, authorizer):
        """Update the saved copy of the refresh token.

        Handle callback that is invoked after a refresh token is used.
        :param authorizer: The ``prawcore.Authorizer`` instance used containing

        ``access_token`` and ``refresh_token`` attributes.
        This function will be called after refreshing the access and refresh
        tokens. This callback can be used for saving the updated
        ``refresh_token``.
        """
        self._current_user.reddit_refresh_token = authorizer.refresh_token
        self._db.commit()
        self._db.refresh(self._current_user)

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
