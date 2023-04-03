import React, { useState } from 'react';

function Vocabulary() {
  const [searchString, setSearchString] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = (event) => {
    const searchString = event.target.value;

    setSearchString(searchString);

    if (searchString.length > 2) {
      // Lakukan pencarian hanya jika panjang kata kunci lebih dari 2 karakter

      // Implementasi kode untuk melakukan pencarian kosa kata berdasarkan API
      fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${searchString}`)
        .then((response) => response.json())
        .then((data) => {
          // Ambil definisi dari hasil pencarian API
          const definitions = data[0].meanings.map((meaning) => meaning.definitions[0].definition);

          // Simpan hasil pencarian pada state searchResults
          setSearchResults([
            {
              id: 1,
              word: searchString,
              definition: definitions.join(', ')
            }
          ]);
        })
        .catch((error) => {
          console.error(error);
          setSearchResults([]);
        });
    } else {
      // Bersihkan hasil pencarian jika panjang kata kunci kurang dari atau sama dengan 2 karakter
      setSearchResults([]);
    }
  };

  return (
    <div className="container">
      
      <input type="text" className="form-control mb-2" placeholder="Ketik kata kunci..." value={searchString} onChange={handleSearch} />
      <ul>
          {searchResults.map((result) => (
            <li key={result.id}>
              <li>{result.word}</li>
              <li>{result.definition}</li>
            </li>
          ))}
</ul>
    </div>
  );
}

export default Vocabulary;
