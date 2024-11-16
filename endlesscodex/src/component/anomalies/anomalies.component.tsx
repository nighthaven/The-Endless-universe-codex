import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../../store/store';
import { fetchAnomalies } from '../../store/anomalies/anomalies.reducer';
import ItemLayoutComponent from '../itemlayout/item-layout.component';

import {
  InfoContainer,
  ImageContainerAnomaly,
  ImageBackground,
} from './anomalies.styles';

function AnomaliesComponent() {
  const dispatch = useDispatch<AppDispatch>();

  const { anomalies, error } = useSelector(
    (state: RootState) => state.anomalies
  );

  useEffect(() => {
    dispatch(fetchAnomalies());
  }, [dispatch]);

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <>
      {anomalies.map((anomaly) => (
        <ItemLayoutComponent key={anomaly.id}>
          <InfoContainer>
            <h2 className="info-container-h2">{anomaly.name}</h2>
            <p className="info-p">{anomaly.description}</p>
            <ImageContainerAnomaly>
              <ImageBackground imageUrl={anomaly.image} />
            </ImageContainerAnomaly>
          </InfoContainer>
        </ItemLayoutComponent>
      ))}
    </>
  );
}

export default AnomaliesComponent;
