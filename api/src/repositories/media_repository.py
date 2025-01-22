from src.models.media_models import Media
from src.repositories.base_repository import BaseRepository


class MediaRepository(BaseRepository):

    def get_all(self):
        media = self.db.query(Media).all()
        return media

    def get_by_name(self, name):
        media = self.db.query(Media).filter(Media.name == name).first()
        return media
