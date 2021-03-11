import { ChangeEvent, FormEvent, useState } from 'react';

type FormProps = {
    setAuthToken(arg: string): void;
};

const Form = ({ setAuthToken }: FormProps): JSX.Element => {
    const [formData, setFormData] = useState({ username: '', password: '' });

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

    const loginRequest = async (): Promise<void> => {
        const formDataObj = new FormData();
        formDataObj.append('username', formData.username);
        formDataObj.append('password', formData.password);

        const options = {
            method: 'POST',
            body: formDataObj,
        };

        const response = await fetch('http://localhost:8000/api/token', options);
        const data = await response.json();
        setAuthToken(data.access_token);
    };

    return (
        <>
            <h1>Login Form</h1>
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
                <input type='submit' />
            </form>
        </>
    );
};

export default Form;
