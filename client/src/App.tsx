import { useState } from 'react';
import Form from 'components/form/Form';
import LinkRedditForm from 'LinkRedditForm';

function App(): JSX.Element {
    const [token, setAuthToken] = useState<string>('');

    return (
        <>
            <h1>App Component</h1>
            {token ? <LinkRedditForm /> : <Form setAuthToken={setAuthToken} />}
        </>
    );
}

export default App;
