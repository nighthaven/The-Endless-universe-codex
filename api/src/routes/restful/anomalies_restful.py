from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Query
from src.models.anomalies_models import Anomaly
from src.repositories.anomaly_repository import AnomalyRepository

router = APIRouter(
    prefix="/endless/anomalies",
    tags=["anomalies"],
)


@router.get("/")
def list_anomalies(
    anomaly_repository: AnomalyRepository = Depends(AnomalyRepository),
):
    anomalies_list: Query[Anomaly] = anomaly_repository.get_all()  # type: ignore[no-untyped-call]
    return {
        "count": anomalies_list.count(),
        "results": [
            {"name": anomaly.name, "url": anomaly.url} for anomaly in anomalies_list
        ],
    }


@router.get("/{anomaly_id}/")
def get_anomaly(
    anomaly_id: int, anomaly_repository: AnomalyRepository = Depends(AnomalyRepository)
):
    anomaly = anomaly_repository.find_by_id(anomaly_id)
    if not anomaly:
        raise HTTPException(status_code=404, detail="Anomaly not found")
    return {
        "id": anomaly.id,
        "name": anomaly.name,
        "description": anomaly.description,
        "image": anomaly.image,
        "url": anomaly.url,
        "media_id": anomaly.media_id,
        "media": anomaly.media.name,  # type: ignore[attr-defined]
    }
