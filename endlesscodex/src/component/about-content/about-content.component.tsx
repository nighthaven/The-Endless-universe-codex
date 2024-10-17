import ItemLayoutComponent from "../itemlayout/item-layout.component";

import "./about-content.styles.scss"


const AboutContentComponent = () => {
    return (
        <div className="about-component-parent">
            <ItemLayoutComponent>
                <div className="about-component-window">
                    <div className="about-component-window-header">
                        <h2 className="about-component-h2">Title is a superbe title</h2>
                        <p className="about-component-p"> This is a superbe paragraphe</p>
                    </div>
                    <div className="about-component-content">test test lorem ipsum</div>
                    <p className="about-component-text-foreground">
                        2024-10-01
                    </p>
                </div>
            </ItemLayoutComponent>
        </div>

    )
}


export default AboutContentComponent