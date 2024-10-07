from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session

from src.models import get_db
from src.models.media_models import Media
from src.serializer.media_serializer import MediaFormCreation


class MediaService:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    @staticmethod
    def create(media: MediaFormCreation, db: Session):
        new_media = Media(
            name=media.name,
            description=media.description,
        )
        db.add(new_media)
        db.commit()
        db.refresh(new_media)
        return new_media


    def get_all(self):
        media = self.db.query(Media).all()
        return media