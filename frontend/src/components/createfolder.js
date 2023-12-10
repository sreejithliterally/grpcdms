import React, { useState } from 'react';
import './createfolder.css';
import axios from 'axios';


const CreateFolder = () => {
  const [folderName, setFolderName] = useState('');


  const handleCreateFolder = async () => {
    try {
      const token = localStorage.getItem('token');

      // Create form data
      const formData = new FormData();
      formData.append('folder_name', folderName);

      const response = await axios.post(
        'http://127.0.0.1:8000/create_folder',
        formData,  // Send form data
        {
          headers: {
            'Content-Type': 'multipart/form-data',  // Set the Content-Type header for form data
            'x-token': token,
            Authorization: `Bearer ${token}`,
          },
        }
      );

      console.log(response.data);

      

      // Handle success or show a notification
    } catch (error) {
      console.error('Error creating folder:', error);

      // Handle error or show a notification
    }
  };

  return (
    <div>
      <input
        type='text'
        placeholder='Enter folder name'
        value={folderName}
        onChange={(e) => setFolderName(e.target.value)}
      />
      <button className='log' onClick={handleCreateFolder}>
        Create Folder
      </button>
    </div>
  );
};

export default CreateFolder;
