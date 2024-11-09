import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import './App.css';
import './component/firefly/firefly.component';
import Home from './routes/home/home-page.component';
import AboutComponent from './routes/about/about-page.component';
import AnomaliesPage from './routes/anomalies/anomalies-page.component';
import FactionPageComponent from './routes/factions/factions-page.component';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/factions" element={<FactionPageComponent />} />
        <Route path="/anomalies" element={<AnomaliesPage />} />
        <Route path="/about" element={<AboutComponent />} />
      </Routes>
    </Router>
  );
}

export default App;
