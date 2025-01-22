from typing import Optional

from src.enums.media_name import MediaName
from src.models.media_models import Media
from src.models.wonders_models import Wonder
from src.repositories.base_repository import BaseRepository


class WonderRepository(BaseRepository):

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
