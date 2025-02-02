import BackgroundComponent from '../../component/background/background.component';
import HomeComponent from '../../component/home/home.component';

import Title from './home-page.styles';

function Home() {
  return (
    <BackgroundComponent>
      <Title>
        <h1>API Resources</h1>
      </Title>
      <HomeComponent />
    </BackgroundComponent>
  );
}

export default Home;
