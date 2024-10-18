from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session
from src.models import get_db
from src.models.anomalies_models import Anomaly


class AnomalyService:
    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        self.db = db

    def create(self, anomaly: Anomaly):
        self.db.add(anomaly)
        self.db.commit()
        self.db.refresh(anomaly)
        return anomaly

    def get_all(self):
        anomaly = self.db.query(Anomaly).all()
        return anomaly
