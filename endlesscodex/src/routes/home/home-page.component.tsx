import { Outlet } from 'react-router-dom';

import FireflyComponent from "../../component/firefly/fireflyComponent";
import NavbarComponent from "../navbar/navbar.component";

const Home = () => {
  return (
    <div className="background">
      <FireflyComponent />
      <NavbarComponent />
    </div>
  );
};

export default Home;
