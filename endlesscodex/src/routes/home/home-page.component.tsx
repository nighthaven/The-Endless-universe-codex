import BackgroundComponent from '../../component/background/background.component';
import HomeComponent from '../../component/home/home.component';

function Home() {
  return (
    <BackgroundComponent>
      <h1>Documentation de l&apos;API</h1>
      <HomeComponent />
    </BackgroundComponent>
  );
}

export default Home;
