import './about.styles.scss';
import AboutContentComponent from '../../component/about-content/about-content.component';
import BackgroundComponent from '../../component/background/background.component';

function AboutComponent() {
  return (
    <BackgroundComponent>
      <AboutContentComponent />
    </BackgroundComponent>
  );
}

export default AboutComponent;
