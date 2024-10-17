import React from 'react';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import './App.css';
import "./component/firefly/fireflyComponent";
import Home from "./routes/home/home.component";
import AboutComponent from "./routes/about/about";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
          <Route path="/about" element={<AboutComponent />} />
      </Routes>
    </Router>
  );
}

export default App;
