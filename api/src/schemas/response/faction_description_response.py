from typing import List

from pydantic import ConfigDict
from src.schemas.base.faction_base import FactionDescriptionBase


class FactionDescriptionResponse(FactionDescriptionBase):
    description: str
    government: str
    ideology: str
    home_planet: str
    affinity: List[str]
    populations: List[str]
    traits: List[str]
    starting_technology: List[str]
    units: List[str]
    heroes: List[str]

    model_config = ConfigDict(from_attributes=True)
