import React from 'react';
import './background.styles.scss'

import FireflyComponent from "../firefly/fireflyComponent";
import NavbarComponent from "../../routes/navbar/navbar.component";
import {BorderParent} from "../../routes/anomalies/anomalies-page.styles";

const BackgroundComponent: React.FC<{ children?: React.ReactNode }> = ({ children })  => {
    return (
        <div className="background">
            <FireflyComponent data-testid="firefly-component"/>
            <NavbarComponent data-testid="navbar-component"/>
            <BorderParent />
            <div className="content">{children}</div>
        </div>
    )
}

export default BackgroundComponent