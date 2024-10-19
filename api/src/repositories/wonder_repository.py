from typing import Annotated, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from src.enums.media_name import MediaName
from src.models import get_db
from src.models.media_models import Media
from src.models.wonders_models import Wonder


class WonderRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, wonder: Wonder):
        self.db.add(wonder)
        self.db.commit()
        self.db.refresh(wonder)
        return wonder

    def find_all(
        self,
        media: Optional[MediaName] = None,
        wonder_name: Optional[str] = None,
    ):
        wonder_query = self.db.query(Wonder)
        if wonder_name:
            wonder_query = wonder_query.filter(Wonder.name.ilike(f"%{wonder_name}%"))
        if media:
            media_query = self.db.query(Media).filter(Media.name == media).one()
            wonder_query = wonder_query.filter(Wonder.media_id == media_query.id)
        return wonder_query.all()
