from typing import Annotated, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, joinedload
from src.enums.media_name import MediaName
from src.models import get_db
from src.models.faction_description_model import FactionDescription
from src.models.factions_models import Faction
from src.models.media_models import Media


class FactionDescriptionRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def get_all(self):
        return self.db.query(FactionDescription).order_by(FactionDescription.id)

    def find_by_id(
        self,
        faction_description_id: int,
    ) -> Optional[FactionDescription]:
        return (
            self.db.query(FactionDescription)
            .filter(FactionDescription.id == faction_description_id)
            .one_or_none()
        )

    def find_by(
        self,
        media: Optional[MediaName] = None,
        faction_name: Optional[str] = None,
    ):
        faction_description_query = self.db.query(FactionDescription).options(
            joinedload(FactionDescription.faction), joinedload(FactionDescription.media)
        )
        if faction_name:
            faction_description_query = faction_description_query.join(Faction).filter(
                Faction.name.ilike(f"%{faction_name}%")
            )
        if media:
            faction_description_query = faction_description_query.join(Media).filter(
                Media.name == media
            )
        return faction_description_query.all()
