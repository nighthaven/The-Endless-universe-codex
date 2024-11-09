import React, { Fragment, useEffect, useState } from 'react';
import axios from 'axios';

import ItemLayoutComponent from "../itemlayout/item-layout.component";

import {Title, InfoContainer, ImageContainerFaction, InfoText, RightInformation, ImageBackground} from "./factions-list.styles"

interface Faction {
  id: number;
  faction: {
    name: string;
  };
  media: {
    name: string;
  };
  description: string;
  image_url: string;
  government: string;
  ideology: string;
  home_planet: string;
  affinity: string[];
  populations: string[];
  traits: string[];
  starting_technology: string[];
  units: string[];
  heroes: string[];
  major: boolean;
}

const apiUrl = `${process.env.REACT_APP_API_BASE_URL}/factions`;

const FactionListComponent: React.FC = () => {
  const [factions, setFactions] = useState<Faction[]>([]);

  const fetchFactions = async () => {
    try {
      const response = await axios.get<Faction[]>(apiUrl);
      setFactions(response.data);
    } catch (error) {
      alert("Une erreur est survenue lors de la récupération des données. Veuillez réessayer.");
    }
  };


  useEffect(() => {
    fetchFactions();
  }, []);

  return (
    <Fragment>
      <Title><h1>Liste des Factions</h1></Title>
      {factions.length > 0 ? (
        factions.map((faction) => (
          <ItemLayoutComponent key={faction.id}>
            <InfoContainer>
              <InfoText>
                <h2 data-testid="faction">{faction.faction.name}</h2>
                <p><span>Description:</span> {faction.description}</p>
                <br/>
                <br/>
                <p><span>Affinité:</span> {faction.affinity?.join(', ')}</p>
                <p><span>Traits:</span> {faction.traits?.join(', ')}</p>
                <p><span>Technologie de départ:</span> {faction.starting_technology?.join(', ')}</p>
                <p><span>Units:</span> {faction.units?.join(', ')}</p>
                {faction.heroes.length > 0 && (<p><span>Heroes:</span> {faction.heroes}</p>)}
              </InfoText>
              <RightInformation>
                <h2>{faction.media.name}</h2>
                <p>{faction.major ? 'Major' : 'Minor'} faction</p>
                <ImageContainerFaction>
                  <ImageBackground imageUrl={faction.image_url}/>
                </ImageContainerFaction>
                {faction.government && (<p><span>Gouvernement:</span> {faction.government}</p>)}
                {faction.ideology && (<p><span>Ideology:</span> {faction.ideology}</p>)}
                {faction.home_planet && (<p><span>Home planet:</span> {faction.home_planet}</p>)}
                {faction.populations.length > 0 && (<p><span>Populations:</span> {faction.populations?.join(', ')}</p>)}
              </RightInformation>
            </InfoContainer>
          </ItemLayoutComponent>
        ))
      ) : (
        <p>Aucune faction trouvée.</p>
      )}
    </Fragment>
  );
};

export default FactionListComponent;
