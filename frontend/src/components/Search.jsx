import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {InputText} from 'primereact/inputtext';
import { Button } from 'primereact/button';

function Search() {
  const [username, setUsername] = useState('');
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    try {
      setLoading(true);
      setError('');

      const response = await axios.get(`http://13.239.136.211/api/blog/list/users?username=${username}`);
      // console.log(response.data);
      setUserData(response.data);
    } catch (error) {
      setError('Username tidak ditemukan');
    } finally {
      setLoading(false);
    }
  };
// const [pengguna, setPengguna] = useState([]);
// const [query, setQuery] = useState("");
// const penggunas = Array.from(pengguna);

//  useEffect(() => {
//     fetch('http://13.239.136.211/api/blog/list/users')
//       .then(response => response.json())
//       .then(data => setPengguna(data));
//   }, []);

//   const handleChange = event => {
//     setQuery(event.target.value);
//   };

//   const filteredUsers = penggunas.filter(user => {
//     return user.username.toLowerCase().includes(query.toLowerCase());
//   });
  return (
    <>
      <div>
        <span className='p-input-icon-left'>
        <InputText
         type="text" 
         style={{width:"700px"}} 
         className="form-control" 
         placeholder="cari sesuatu..." 
        //  value={searchValue} 
         onChange={(e) => setUsername(e.target.value)} 
         value={username}
         />
        </span>
        <Button onClick={handleSearch} disabled={loading}>
        {loading ? 'Loading...' : 'Search'}
      </Button>
      </div>
      <div>
      {error && <p>{error}</p>}
      {userData && (
        <div>
          <h2>User Data</h2>
          <p>Name: {userData.name}</p>
          <p>Email: {userData.email}</p>
          {/* Tambahkan properti data lain yang ingin ditampilkan */}
        </div>
      )}

      </div>
    </>
  );
}

export default Search;
