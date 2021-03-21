/*
TODO:

  * func will to trigger OAuth request via backend and return OAuthURL
  * client will be redirected to Reddit to grant application permission
  * backend will listen auto redirect on approval to store token
**/
import { useState } from 'react';

type LinkRedditFormProps = {
    token: string;
};

const LinkRedditForm = ({ token }: LinkRedditFormProps): JSX.Element => {
    const [authLink, setAuthLink] = useState('https://www.reddit.com/api');

    const redditOAuthHandler = async () => {
        const options = {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        };
        const response = await fetch('http://localhost:8000/api/reddit/authenticate', options);
        const link = await response.json();
        setAuthLink(link);
    };

    const clickHandler = async () => {
        const options = {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        };
        const response = await fetch('http://localhost:8000/api/reddit', options);
        const data = await response.json();
        console.log('clicked', data);
    };

    return (
        <>
            <h1>Link Reddit Form</h1>
            <button type='button' onClick={redditOAuthHandler}>
                Link your Reddit Account
            </button>
            <a target='_blank' rel='noreferrer' href={authLink}>
                Hi
            </a>
            <button onClick={clickHandler}>Test</button>
        </>
    );
};

export default LinkRedditForm;
