import React, {Fragment, useEffect, useState} from "react";
import ItemLayoutComponent from "../itemlayout/item-layout.component";
import aboutImage from "../../img/about.png";
import aboutFlickeringImage from "../../img/about-flickering.png";

import "./about-content.styles.scss";

const AboutContentComponent = () => {
    const images = [aboutImage, aboutFlickeringImage];
    const [currentImageIndex, setCurrentImageIndex] = useState(0);

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentImageIndex(1);

            const flickerInterval = setInterval(() => {
                setCurrentImageIndex((prevIndex) => (prevIndex === 0 ? 1 : 0));
            }, 50);

            setTimeout(() => {
                clearInterval(flickerInterval);
                setCurrentImageIndex(1);

                setTimeout(() => {
                    setCurrentImageIndex(0);
                }, 1500);
            }, 500);
        }, 5000);

        return () => clearInterval(interval);
    }, []);

    return (
        <Fragment>
            <div className="about-content" data-testid="about">
                <ItemLayoutComponent className="About-image_layout">
                    <div className="about-image-container">
                        <img
                            src={images[currentImageIndex]}
                            alt="About slideshow"
                            className="about-image"
                        />
                    </div>
                </ItemLayoutComponent>
                <ItemLayoutComponent className="about-text">
                    <div className="about-component-window">
                        <div className="about-component-window-header">
                            <h2 className="about-component-h2">About</h2>
                            <p className="about-component-p"> My name is Boris, I am a developer, this is one of my
                                multiple projects.</p>
                            <br/>
                            <p className="about-component-p">This website is a fanbase of the universe of amplitude, made with FastAPI and React.
                                The goal is, when finish, to have like an API where any user should be able to search for lore information about the endless universe.</p>
                            <br/>
                            <p className="about-component-p">Thanks a lot to all the staff of Amplitude Studio who answer me about these information, this website has been made with their agreement.</p>
                        </div>
                        <div className="about-component-content"></div>
                        <p className="about-component-text-foreground"></p>
                    </div>
                </ItemLayoutComponent>
                </div>
        </Fragment>
    );
};

export default AboutContentComponent;
