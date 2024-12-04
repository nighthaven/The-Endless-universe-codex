import React, { useEffect, useState } from 'react';

function OpenApiViewer() {
  const [openApiData, setOpenApiData] = useState(null);
  const [error, setError] = useState<string | null>(null);
  const [inputUrl, setInputUrl] = useState('');
  const [apiUrl, setApiUrl] = useState(
    `${process.env.REACT_APP_API_BASE_URL}/openapi.json`
  );

  const baseUrl = process.env.REACT_APP_API_BASE_URL || '';

  useEffect(() => {
    if (!apiUrl) return;

    fetch(apiUrl)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setOpenApiData(data);
        setError(null);
      })
      .catch((err) => {
        setError(`Erreur lors de la récupération des données : ${err.message}`);
        setOpenApiData(null);
      });
  }, [apiUrl]);

  const handleFormSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (inputUrl.trim()) {
      setApiUrl(`${baseUrl}${inputUrl}`);
    } else {
      setApiUrl(`${baseUrl}/openapi.json`);
    }
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit} style={{ marginBottom: '16px' }}>
        <div
          style={{ display: 'flex', alignItems: 'center', marginBottom: '8px' }}
        >
          <span
            style={{
              padding: '8px',
              backgroundColor: '#f0f0f0',
              border: '1px solid #ddd',
              borderRadius: '4px 0 0 4px',
              fontWeight: 'bold',
            }}
          >
            {baseUrl}
          </span>
          <input
            type="text"
            value={inputUrl}
            onChange={(e) => setInputUrl(e.target.value)}
            placeholder="Entrez un chemin (ex: /factions)"
            style={{
              flex: 1,
              padding: '8px',
              border: '1px solid #ddd',
              borderRadius: '0 4px 4px 0',
            }}
          />
        </div>
        <button
          type="submit"
          style={{
            padding: '8px 16px',
            backgroundColor: '#007bff',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Charger
        </button>
      </form>

      <div
        style={{
          maxWidth: '800px',
          maxHeight: '500px',
          overflowY: 'scroll',
          border: '1px solid #ddd',
          padding: '16px',
          backgroundColor: '#f9f9f9',
        }}
      >
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {openApiData ? (
          <pre>{JSON.stringify(openApiData, null, 2)}</pre>
        ) : (
          <p>Chargement des données...</p>
        )}
      </div>
    </div>
  );
}

export default OpenApiViewer;
