import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Logout from '../authpages/Logout';
import '../../../node_modules/bootstrap/dist/css/bootstrap.min.css';

function Home() {
  const [folders, setFolders] = useState([]);

  useEffect(() => {
    const fetchFolders = async () => {
      try {
        // Retrieve the token from localStorage
        const token = localStorage.getItem('token');
        console.log('Token:', token); 

       
        const response = await axios.get('http://127.0.0.1:8000/get_folders', {
          headers: {
            Authorization: `${token}`,
          },
        });

        console.log('Folders Response:', response); 

        
        setFolders(response.data.folders);
      } catch (error) {
        console.error('Error fetching folders:', error);
      }
    };

    // Call the fetchFolders function when the component mounts
    fetchFolders();
  }, []);

  console.log('Folders:', folders);

  return (
    <div className='formContainer'>
      <div className='logout'>
        <Logout />
      </div>
      <h1 className='pageTitle'>Store your docs</h1>

      
      <ul>
        {folders.map((folder) => (
          <li key={folder.folder_id}>{folder.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
