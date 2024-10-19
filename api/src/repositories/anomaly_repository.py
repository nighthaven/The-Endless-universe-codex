from typing import Annotated, Optional

from fastapi import Depends
from sqlalchemy.orm import Session
from src.enums.media_name import MediaName
from src.models import get_db
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media


class AnomalyRepository:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def save(self, anomaly: Anomaly):
        self.db.add(anomaly)
        self.db.commit()
        self.db.refresh(anomaly)
        return anomaly

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
