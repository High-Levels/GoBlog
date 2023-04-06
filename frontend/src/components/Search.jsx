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
    <>
      <div>
        <input type="text" style={{width:"700px"}} className="form-control" placeholder="cari sesuatu..." value={searchString} onChange={handleSearch} />
      </div>
      <div>
        {searchResults.map((result) => (
          <div key={result.id}>
            <p><strong>{result.word}</strong> {result.definition}</p>
          </div>
        ))}
      </div>
    </>
  );
}

export default Vocabulary;
