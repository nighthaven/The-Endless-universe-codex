import enum

from sqlalchemy import Column, Enum, Integer, String
from src.models import Base


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
