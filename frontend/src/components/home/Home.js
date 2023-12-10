import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Logout from '../authpages/Logout';
import CreateFolder from '../createfolder';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFolder } from '@fortawesome/free-solid-svg-icons';
import './home.css';

function Home() {
  const [folders, setFolders] = useState([]);

  useEffect(() => {
    const fetchFolders = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://127.0.0.1:8000/get_folders', {
          headers: {
            'x-token': token,
            Authorization: `Bearer ${token}`,
          },
        });

        setFolders(response.data.folders);
      } catch (error) {
        console.error('Error fetching folders:', error);
      }
    };

    fetchFolders();
  }, []);

  return (
    <div className='formContainer'>
      <div className='logout'>
        <Logout />
      </div>
      <div className='createfolder'>
        <CreateFolder />
      </div>
      <h1 className='pageTitle'>Store your docs</h1>

      {folders.length > 0 ? (
        <div className='folderRow'>
          {folders.map((folder) => (
            <div key={folder.folder_id} className='folderItem'>
              <FontAwesomeIcon icon={faFolder} size="4x" color='#F8D775' />
              <p className='foldericon'>{folder.name} </p>
            </div>
          ))}
        </div>
      ) : (
        <p>Loading folders...</p>
      )}
    </div>
  );
}

export default Home;
