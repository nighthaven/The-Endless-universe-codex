from sqlalchemy.orm import Session

from src.models.media_models import Media
from src.serializer.media_serializer import MediaFormCreation


class MediaServices:
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

    @staticmethod
    def get_all(db: Session):
        media = db.query(Media).all()
        return media