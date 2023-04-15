import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Search() {

const [pengguna, setPengguna] = useState([]);
const [query, setQuery] = useState("");
const penggunas = Array.from(pengguna);

 useEffect(() => {
    fetch('http://13.239.136.211/api/blog/list/users')
      .then(response => response.json())
      .then(data => setPengguna(data));
  }, []);

  const handleChange = event => {
    setQuery(event.target.value);
  };

  const filteredUsers = penggunas.filter(user => {
    return user.username.toLowerCase().includes(query.toLowerCase());
  });
  return (
    <>
      <div>
        <input
         type="text" 
         style={{width:"700px"}} 
         className="form-control" 
         placeholder="cari sesuatu..." 
        //  value={searchValue} 
         onChange={handleChange} 
         />
         {/* <button onClick={handleSearch}>cari</button> */}
      </div>
      <div>
        {
          filteredUsers.map(user=>(
            <li key={user.id}>{user.username}</li>
          ))
        }
      </div>
    </>
  );
}

export default Search;
