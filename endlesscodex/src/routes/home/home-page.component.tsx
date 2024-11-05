import BackgroundComponent from "../../component/background/background.component";
import React, { Fragment } from "react";
import HomeComponent from "../../component/home/home.component";
const Home = () => {
  return (
    <Fragment>
        <BackgroundComponent>
            <h1>Documentation de l'API</h1>
            <HomeComponent />
        </BackgroundComponent>
    </Fragment>
  );
};

export default Home;
