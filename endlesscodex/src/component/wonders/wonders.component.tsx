import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState, AppDispatch } from '../../store/store';
import { fetchWonders } from '../../store/wonders/wonders.reducer';
import ItemLayoutComponent from '../itemlayout/item-layout.component';

import {
  InfoContainer,
  ImageContainerAnomaly,
  ImageBackground,
} from './wonders.styles';
import { Title } from '../factions/factions-list.styles';

function WondersComponent() {
  const dispatch = useDispatch<AppDispatch>();

  const { wonders, error } = useSelector((state: RootState) => state.wonders);

  useEffect(() => {
    dispatch(fetchWonders());
  }, [dispatch]);

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <>
      <Title>
        <h1>Wonders</h1>
      </Title>
      <div data-testid="wonder-content">
        {wonders.map((wonder) => (
          <ItemLayoutComponent key={wonder.id}>
            <InfoContainer>
              <h2 className="info-container-h2" data-testid="wonder-name">
                {wonder.name}
              </h2>
              <p className="info-p">{wonder.description}</p>
              <ImageContainerAnomaly>
                <ImageBackground imageUrl={wonder.image} />
              </ImageContainerAnomaly>
            </InfoContainer>
          </ItemLayoutComponent>
        ))}
      </div>
    </>
  );
}

export default WondersComponent;
