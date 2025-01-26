from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import get_db
from src.models.media_models import Media


class MediaRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, media: Media):
        self.db.add(media)
        self.db.commit()
        self.db.refresh(media)
        return media

    def get_all(self) -> list[Media]:
        media = self.db.query(Media).all()
        return media

    def get_by_name(self, name):
        media = self.db.query(Media).filter(Media.name == name).first()
        return media
