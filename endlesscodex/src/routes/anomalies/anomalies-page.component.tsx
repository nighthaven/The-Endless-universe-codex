import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Anomaly {
  id: number;
  name: string;
  description: string;
  image: string;
}

const AnomaliesPage: React.FC = () => {
  const [anomalies, setAnomalies] = useState<Anomaly[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchAnomalies = async () => {
      try {
        const response = await axios.get('/anomalies');
        setAnomalies(response.data);
      } catch (err) {
        setError('Erreur lors de la récupération des anomalies.');
      } finally {
        setLoading(false);
      }
    };

    fetchAnomalies(); // Appel de la fonction lors du premier rendu
  }, []);

  if (loading) {
    return <div>Chargement des anomalies...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }
  return (
    <div>
      <h1>Liste des Anomalies</h1>
      <ul>
        {anomalies.map((anomaly) => (
          <li key={anomaly.id}>
            <h2>{anomaly.name}</h2>
            <p>{anomaly.description}</p>
            {anomaly.image && <img src={`${anomaly.image}`} alt={anomaly.name} />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AnomaliesPage;
