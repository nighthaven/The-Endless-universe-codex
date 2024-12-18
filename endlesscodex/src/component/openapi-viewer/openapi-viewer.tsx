import React, { useEffect, useState } from 'react';

function OpenApiViewer() {
  const [openApiData, setOpenApiData] = useState(null);
  const [error, setError] = useState<string | null>(null);
  const apiUrl = `${process.env.REACT_APP_API_BASE_URL}/openapi.json`;

  useEffect(() => {
    fetch(apiUrl)
      .then((response) => response.json())
      .then((data) => setOpenApiData(data))
      .catch(() => {
        setError('Erreur lors de la récupération du fichier JSON');
      });
  }, []);

  return (
    <div
      style={{
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
        <p>Chargement des données OpenAPI...</p>
      )}
    </div>
  );
}

export default OpenApiViewer;
