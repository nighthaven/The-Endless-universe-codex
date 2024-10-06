from sqlalchemy.orm import Relationship

from sqlalchemy import Column, String, Integer, TIMESTAMP, text, DateTime, Enum, ARRAY, ForeignKey, Boolean
from src.models import Base

from datetime import datetime

class Faction(Base):
    __tablename__ = "factions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)


class FactionDescription(Base):
    __tablename__ = "factions_descriptions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    faction_id = Column(Integer, ForeignKey("factions.id"), nullable=False)
    faction = Relationship("Faction")
    media_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    media = Relationship("Media")
    size = Column(Boolean, nullable=False, server_default="False")
