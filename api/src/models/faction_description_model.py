from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.models import Base
from src.models.factions_models import Faction
from src.models.planets_model import Planet


class FactionDescription(Base):
    __tablename__ = "factions_descriptions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    faction_id = Column(Integer, ForeignKey("factions.id"), nullable=False)
    faction = relationship(Faction)  # type: ignore[misc]
    media_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    media = relationship("Media")  # type: ignore[misc]
    description = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
    government = Column(String, nullable=True)
    ideology = Column(String, nullable=True)
    home_planet_id = Column(Integer, ForeignKey("planet.id"), nullable=True)
    home_planet = relationship(Planet)  # type: ignore[misc]
    affinity = Column(ARRAY(String), nullable=True)
    populations = Column(ARRAY(String), nullable=True)
    traits = Column(ARRAY(String), nullable=True)
    starting_technology = Column(ARRAY(String), nullable=True)
    units = Column(ARRAY(String), nullable=True)
    heroes = Column(ARRAY(String), nullable=True)
    major = Column(Boolean, nullable=False, default=True)
    url = Column(String, nullable=False)
