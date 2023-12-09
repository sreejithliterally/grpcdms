import React from 'react';
import './logout.css'
import { useNavigate } from 'react-router-dom';

const Logout = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div>
      
      <button className='log' onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;
