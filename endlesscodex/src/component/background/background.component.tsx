import React from 'react';
import './background.styles.scss';

import FireflyComponent from '../firefly/firefly.component';
import NavbarComponent from '../../routes/navbar/navbar.component';
import BorderParent from '../../routes/anomalies/anomalies-page.styles';

function BackgroundComponent({
  children = null,
}: {
  children?: React.ReactNode;
}) {
  return (
    <div className="background" data-testid="background">
      <FireflyComponent />
      <NavbarComponent />
      <BorderParent />
      <div className="content">{children}</div>
    </div>
  );
}

BackgroundComponent.defaultProps = {
  children: null,
};

export default BackgroundComponent;
