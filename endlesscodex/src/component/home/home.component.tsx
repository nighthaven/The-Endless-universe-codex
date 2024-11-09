import OpenApiViewer from '../openapi-viewer/openapi-viewer';

import './home.style.scss';

function HomeComponent() {
  return (
    <div className="info-container">
      <OpenApiViewer />
    </div>
  );
}

export default HomeComponent;
