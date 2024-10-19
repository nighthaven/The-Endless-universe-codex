from sqlalchemy import Column, Integer, String
from src.models import Base


class Faction(Base):
    __tablename__ = "factions"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
