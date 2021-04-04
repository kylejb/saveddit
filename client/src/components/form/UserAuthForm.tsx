import { ChangeEvent, FormEvent, useState } from 'react';

type UserAuthFormProps = {
    setAuthToken: (arg: string) => void;
    setFormType: (arg: 'login' | 'signup' | 'done') => void;
    formType: string;
};

const UserAuthForm = ({ setAuthToken, setFormType, formType }: UserAuthFormProps): JSX.Element => {
    const [formData, setFormData] = useState({ username: '', password: '' });

    const loginRequest = async (): Promise<void> => {
        const formDataObj = new FormData();
        formDataObj.append('username', formData.username);
        formDataObj.append('password', formData.password);

        const options = {
            method: 'POST',
            body: formDataObj,
        };
        const URI = formType === 'login' ? 'token' : 'signup';
        const response = await fetch(`http://localhost:8000/api/${URI}`, options);
        const data = await response.json();

        setAuthToken(data.access_token);
        setFormType('done');
    };

    const formInputHandler = (e: ChangeEvent<HTMLInputElement>) => {
        setFormData((prevState) => ({
            ...prevState,
            [e.target.name]: e.target.value,
        }));
    };

    const formSubmitHandler = (e: FormEvent) => {
        e.preventDefault();
        loginRequest();
        setFormData({ username: '', password: '' });
    };

    return (
        <>
            <h1>UserAuth Form</h1>
            <form onSubmit={formSubmitHandler}>
                <input
                    name='username'
                    type='text'
                    value={formData.username}
                    onChange={formInputHandler}
                />
                <br />
                <input
                    name='password'
                    type='password'
                    value={formData.password}
                    onChange={formInputHandler}
                />
                <br />
                <input type='submit' value={formType} />
            </form>
        </>
    );
};

export default UserAuthForm;
