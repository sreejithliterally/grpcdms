import React, { useState } from 'react';
import axios from 'axios';
import './login.css'
import { useNavigate, Link } from 'react-router-dom';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
  
    try {
      const formData = new FormData();
      formData.append('username', email);
      formData.append('password', password);
  
      const response = await axios.post('http://127.0.0.1:8000/login', formData);
  
      // Log the entire response for debugging
      console.log('Login Response:', response);
  
      // Use optional chaining to access the access_token property
      const accessToken = response.data?.token;
  
      if (accessToken) {
        // Log the token and redirect
        console.log("Token stored successfully:", accessToken);
        localStorage.setItem('token', accessToken);
        navigate('/');
      } else {
        // Log an error message if the token is not found in the response
        console.error('Error: Access token not found in the response');
      }
    } catch (error) {
      console.error(error);
    }
  };
  
  

  return (
    <div className="formContainer">
      <div className="formWrapper">
        <span className="logo">gRPC DMS</span>
        <span className="title">Login</span>

        <form onSubmit={handleLogin}>
          <input
            type="text"
            placeholder="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <Link to="/register">Register</Link></p>
      </div>
    </div>
  );
};
export default Login;