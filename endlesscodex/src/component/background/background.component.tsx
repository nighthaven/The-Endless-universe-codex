import React from 'react';
import './background.styles.scss'

import FireflyComponent from "../firefly/fireflyComponent";
import NavbarComponent from "../../routes/navbar/navbar.component";

const BackgroundComponent: React.FC<{ children?: React.ReactNode }> = ({ children })  => {
    return (
        <div className="background">
            <FireflyComponent/>
            <NavbarComponent/>
            <div className="content">{children}</div>
        </div>
    )
}

export default BackgroundComponent