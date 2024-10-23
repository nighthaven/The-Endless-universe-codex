import "./about.styles.scss"
import AboutContentComponent from "../../component/about-content/about-content.component";
import BackgroundComponent from "../../component/background/background.component";
import {Fragment} from "react";

const AboutComponent = () => {
    return (
        <Fragment>
            <BackgroundComponent>
                <AboutContentComponent/>
            </BackgroundComponent>
        </Fragment>
    )
}

export default AboutComponent