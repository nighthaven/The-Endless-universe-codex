import "./about.scss"
import FireflyComponent from "../../component/firefly/fireflyComponent";
import NavbarComponent from "../navbar/navbar.component";
import AboutContentComponent from "../../component/about-content/about-content.component";

const AboutComponent = () => {
    return (
        <div className="background">
            <FireflyComponent/>
            <NavbarComponent/>
            <AboutContentComponent></AboutContentComponent>
        </div>
    )
}

export default AboutComponent