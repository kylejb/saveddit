import { useState } from 'react';
import LoginForm from 'components/form/LoginForm';
import LinkRedditForm from 'LinkRedditForm';

function App(): JSX.Element {
    const [token, setAuthToken] = useState<string>('');

    return (
        <>
            <h1>App Component</h1>
            {token ? <LinkRedditForm /> : <LoginForm setAuthToken={setAuthToken} />}
        </>
    );
}

export default App;
