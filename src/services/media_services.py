from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.models import get_db
from src.models.media_models import Media


class MediaService:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create(self, media: Media):
        self.db.add(media)
        self.db.commit()
        self.db.refresh(media)
        return media

    def get_all(self):
        media = self.db.query(Media).all()
        return media
