/*
TODO:

  * func will to trigger OAuth request via backend and return OAuthURL
  * client will be redirected to Reddit to grant application permission
  * backend will listen auto redirect on approval to store token
**/

function LinkRedditForm() {
    const redditOAuthHandler = async () => null;

    return (
        <>
            <h1>Link Reddit Form</h1>
            <button onClick={redditOAuthHandler}>Link your Reddit Account</button>
        </>
    );
}

export default LinkRedditForm;
