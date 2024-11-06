import React, {Fragment} from "react"
import {Outlet, Link} from "react-router-dom";

import "./navbar.styles.scss"

const NavbarComponent = () => {
    return (
        <Fragment>
            <div className="navigation" data-testid="navbar">
                <Link className="logo-container" to="/">
                    <div className="logo"></div>
                </Link>
                <div className="links-container">
                    <Link className="nav-links" to="/factions">Factions</Link>
                </div>
                <div className="links-container">
                    <Link className="nav-links" to="/anomalies">Anomalies/wonders</Link>
                </div>
                <div className="links-container">
                    <Link className="nav-links" to="/about">About</Link>
                </div>
            </div>
            <Outlet/>
        </Fragment>
    )
}

export default NavbarComponent;