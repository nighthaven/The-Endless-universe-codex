import React, { useEffect, useState } from 'react';

import './restful-viewer.styles.scss';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

type ApiResponse =
  | { count?: number; results?: Record<string, unknown>[] }
  | Record<string, unknown>;

function RestfulViewerComponent() {
  const [data, setData] = useState<ApiResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [searchTerm, setSearchTerm] = useState<string>(
    `${API_BASE_URL}/endless`
  );
  const [query, setQuery] = useState<string>('');

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await fetch(searchTerm);
        if (!response.ok) {
          throw new Error('Erreur de chargement des données');
        }
        const result: ApiResponse = await response.json();
        setData(result);
      } catch (err) {
        setError((err as Error).message);
      }
      setLoading(false);
    };

    fetchData();
  }, [searchTerm]);

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSearchTerm(`${API_BASE_URL}/endless/${query}`);
  };

  return (
    <div className="restful-container">
      <form onSubmit={handleSearchSubmit} className="restful-form">
        <span className="restful-prefix">{API_BASE_URL}/endless/</span>
        <input
          type="text"
          value={query}
          onChange={handleSearchChange}
          className="restful-input"
          placeholder="Rechercher une route (ex: /anomalies)"
        />
        <button type="submit" className="restful-button">
          Rechercher
        </button>
      </form>

      <div className="restful-results">
        {loading && <p>Chargement des données...</p>}
        {error && <p className="restful-error">{error}</p>}
        {data && (
          <pre className="restful-pre">{JSON.stringify(data, null, 2)}</pre>
        )}
      </div>
    </div>
  );
}

export default RestfulViewerComponent;
