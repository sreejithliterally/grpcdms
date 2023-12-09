import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link} from 'react-router-dom';

const Register = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
  
    try {
      const data = {
        username: email,  // Rename email to username if that's the expected field name
        password: password,
      };
  
      const response = await axios.post('http://127.0.0.1:8000/create_user', data);
  
      if (response.status === 200) {
        const result = response.data;
        navigate('/login');
      } else {
        throw new Error('data error');
      }
    } catch (error) {
      console.error(error);
    }
  };
  

  return (
    <div className="formContainer">
      <div className="formWrapper">
        <span className="logo">gRPC DMS</span>
        <span className="title">Register</span>

        <form onSubmit={handleRegister}>
          <input
            type="email"
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

          <button type="submit">Sign up</button>
        </form>
        <p>Have an account already? <Link to="/login">Login</Link></p>
      </div>
    </div>
  );
};

export default Register;
