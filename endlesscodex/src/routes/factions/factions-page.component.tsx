import BackgroundComponent from '../../component/background/background.component';
import { BorderParent } from '../anomalies/anomalies-page.styles';

import FactionsComponent from '../../component/factions/factions-list.component';

function FactionPageComponent() {
  return (
    <BackgroundComponent>
      <BorderParent />
      <FactionsComponent />
    </BackgroundComponent>
  );
}

export default FactionPageComponent;
