from typing import Annotated, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import get_db
from src.models.planets_model import Planet


class PlanetRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, planet: Planet) -> Planet:
        self.db.add(planet)
        self.db.commit()
        self.db.refresh(planet)
        return planet

    def get_all(self):
        return self.db.query(Planet).order_by(Planet.id)

    def find_by_id(
        self,
        planet_id: int,
    ) -> Optional[Planet]:
        return self.db.query(Planet).filter(Planet.id == planet_id).one_or_none()
