from sqlalchemy import Column, Enum, Integer, String
from src.enums.media_name import MediaName
from src.models import Base


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Enum(MediaName), nullable=False)
    description = Column(String)
