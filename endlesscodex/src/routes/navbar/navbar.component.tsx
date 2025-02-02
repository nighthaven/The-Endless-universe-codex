import React, { Fragment } from 'react';
import { Outlet, Link } from 'react-router-dom';

import './navbar.styles.scss';

function NavbarComponent() {
  return (
    <>
      <div className="navigation" data-testid="navbar">
        <Link className="logo-container" to="/">
          <div className="logo" />
        </Link>
        <div className="links-container">
          <Link className="nav-links" to="/factions">
            Factions
          </Link>
        </div>
        <div className="links-container">
          <Link className="nav-links" to="/anomalies">
            Anomalies
          </Link>
        </div>
        <div className="links-container">
          <Link className="nav-links" to="/wonders">
            Wonders
          </Link>
        </div>
        <div className="links-container">
          <Link className="nav-links" to="/about">
            About
          </Link>
        </div>
      </div>
      <Outlet />
    </>
  );
}

export default NavbarComponent;
