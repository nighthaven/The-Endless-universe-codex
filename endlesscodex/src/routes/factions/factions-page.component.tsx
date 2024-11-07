import React, {Fragment} from "react";
import BackgroundComponent from "../../component/background/background.component";
import {BorderParent} from "../anomalies/anomalies-page.styles";

import FactionsComponent from "../../component/factions/factions-list.component";

const FactionPageComponent = () => {
    return (
        <Fragment>
            <BackgroundComponent>
                <BorderParent />
                    <FactionsComponent />
            </BackgroundComponent>
        </Fragment>
    )
}

export default FactionPageComponent