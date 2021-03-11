/*
TODO:

  * func will to trigger OAuth request via backend and return OAuthURL
  * client will be redirected to Reddit to grant application permission
  * backend will listen auto redirect on approval to store token
**/

const LinkRedditForm = (): JSX.Element => {
    const redditOAuthHandler = async () => null;

    return (
        <>
            <h1>Link Reddit Form</h1>
            <button type='button' onClick={redditOAuthHandler}>
                Link your Reddit Account
            </button>
        </>
    );
};

export default LinkRedditForm;
