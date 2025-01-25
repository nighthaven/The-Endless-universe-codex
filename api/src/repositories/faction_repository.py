from typing import Annotated, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import get_db
from src.models.factions_models import Faction


class FactionRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, faction: Faction) -> Faction:
        self.db.add(faction)
        self.db.commit()
        self.db.refresh(faction)
        return faction

    def get_all(self):
        return self.db.query(Faction).order_by(Faction.id)

    def find_by_id(
        self,
        faction_id: int,
    ) -> Optional[Faction]:
        return self.db.query(Faction).filter(Faction.id == faction_id).one_or_none()
