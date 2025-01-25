from sqlalchemy import Column, Integer, String, Text
from src.models import Base


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    type = Column(String, nullable=True)
    description = Column(Text, nullable=False)
    url = Column(String, nullable=False)
