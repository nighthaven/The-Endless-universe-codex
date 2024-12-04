from typing import List, Optional

from pydantic import ConfigDict
from src.schemas.base.faction_base import FactionDescriptionBase
from src.schemas.response.planet_response import PlanetResponse


class FactionDescriptionResponse(FactionDescriptionBase):
    description: str
    government: str
    ideology: str
    home_planet: Optional[PlanetResponse]
    affinity: List[str]
    populations: List[str]
    traits: List[str]
    starting_technology: List[str]
    units: List[str]
    heroes: List[str]
    url: Optional[str]

    model_config = ConfigDict(from_attributes=True)
