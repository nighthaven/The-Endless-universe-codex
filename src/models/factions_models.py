from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Relationship

from src.models import Base


class Faction(Base):
    __tablename__ = "factions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)


class FactionDescription(Base):
    __tablename__ = "factions_descriptions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    faction_id = Column(Integer, ForeignKey("factions.id"), nullable=False)
    faction = Relationship("Faction")  # type: ignore[misc]
    media_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    media = Relationship("Media")  # type: ignore[misc]
    size = Column(Boolean, nullable=False, server_default="False")
