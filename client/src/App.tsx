import { useState } from 'react';
import LinkRedditForm from 'LinkRedditForm';
import UserAuthForm from 'components/form/UserAuthForm';

function App(): JSX.Element {
    const [token, setAuthToken] = useState<string>('');
    const [formType, setFormType] = useState<'login' | 'signup' | 'done'>('login');

    return (
        <>
            <h1>App Component</h1>

            {token ? (
                <LinkRedditForm />
            ) : (
                <>
                    <UserAuthForm
                        formType={formType}
                        setFormType={setFormType}
                        setAuthToken={setAuthToken}
                    />
                    <button
                        type='button'
                        onClick={() => {
                            if (formType === 'signup') {
                                setFormType('login');
                            } else {
                                setFormType('signup');
                            }
                        }}
                    >
                        {formType === 'login' ? 'New User?' : 'Existing User?'}
                    </button>
                </>
            )}
        </>
    );
}

export default App;
