import React from 'react';
import './background.styles.scss'

import FireflyComponent from "../firefly/fireflyComponent";
import NavbarComponent from "../../routes/navbar/navbar.component";
import {BorderParent} from "../../routes/anomalies/anomalies-page.styles";

const BackgroundComponent: React.FC<{ children?: React.ReactNode }> = ({ children })  => {
    return (
        <div className="background">
            <FireflyComponent/>
            <NavbarComponent/>
            <BorderParent />
            <div className="content">{children}</div>
        </div>
    )
}

export default BackgroundComponent