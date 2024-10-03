import enum
import uuid
import typing
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, String, Integer, TIMESTAMP, text, DateTime, Enum, ARRAY
from src.models import Base

from datetime import datetime

class MediaName(enum.Enum):
    ENDLESS_SPACE = "Endless Space"
    ENDLESS_SPACE_2 = "Endless Space 2"
    ENDLESS_LEGEND = "Endless Legend"
    DUNGEON_OF_THE_ENDLESS = "Dungeon Of The Endless"
    ENDLESS_DUNGEON = "Endless Dungeon"


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(MediaName), nullable=False)
    description = Column(String)