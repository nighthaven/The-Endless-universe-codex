import {Fragment} from "react";
import OpenApiViewer from "../openapi-viewer/openapi-viewer";

import "./home.style.scss"

const HomeComponent = () => {
    return (
        <Fragment>
            <div className="info-container">
                <OpenApiViewer/>
            </div>
        </Fragment>
    )
}

export default HomeComponent