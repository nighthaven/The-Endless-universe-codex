from typing import Optional
from src.enums.media_name import MediaName
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media
from src.repositories.base_repository import BaseRepository


class AnomalyRepository(BaseRepository):

    def find_by(
        self,
        media: Optional[MediaName] = None,
        anomaly_name: Optional[str] = None,
    ):
        anomalies_query = self.db.query(Anomaly)
        if anomaly_name:
            anomalies_query = anomalies_query.filter(
                Anomaly.name.ilike(f"%{anomaly_name}%")
            )
        if media:
            media_query = self.db.query(Media).filter(Media.name == media).one()
            anomalies_query = anomalies_query.filter(Anomaly.media_id == media_query.id)
        return anomalies_query.all()
