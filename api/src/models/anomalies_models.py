from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.models import Base


class Anomaly(Base):
    __tablename__ = "anomaly"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    url = Column(String, nullable=False)

    media_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    media = relationship("Media", backref="anomalies")  # type: ignore[misc]
