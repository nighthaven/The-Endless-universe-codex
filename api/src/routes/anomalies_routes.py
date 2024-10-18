from typing import Annotated, Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from src.models import get_db
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media, MediaName
from src.models.users_models import User
from src.serializer.anomalies_serializer import AnomalyBase, AnomalyResponseModel
from src.services.anomaly_services import AnomalyService
from src.utils.Oauth2 import get_current_user

router = APIRouter(
    prefix="/anomalies",
    tags=["anomalies"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_anomaly(
    media_service: Annotated[Any, Depends(AnomalyService)],
    anomalyFormCreation: AnomalyBase,
    db: Annotated[Session, Depends(get_db)],
    current_user: User = Depends(get_current_user),
):
    media = db.query(Media).filter(Media.name == anomalyFormCreation.media_name).first()
    if not media:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="media not found"
        )

    new_anomaly = Anomaly(
        name=anomalyFormCreation.name,
        description=anomalyFormCreation.description,
        image=anomalyFormCreation.image,
        media_id=media.id,
    )
    new_anomaly = media_service.create(new_anomaly)
    return new_anomaly


@router.get("/", response_model=List[AnomalyResponseModel])
def get_all_anomalies(
    db: Annotated[Session, Depends(get_db)],
    media: Optional[MediaName] = None,
    anomaly_name: Optional[str] = None,
) -> List[AnomalyResponseModel]:
    anomalies_query = db.query(Anomaly).options(joinedload(Anomaly.media))
    if anomaly_name:
        anomalies_query = anomalies_query.filter(
            Anomaly.name.ilike(f"%{anomaly_name}%")
        )
    if media:
        media_query = db.query(Media).filter(Media.name == media).one()
        anomalies_query = anomalies_query.filter(Anomaly.media_id == media_query.id)
    anomalies = anomalies_query.all()
    return [
        AnomalyResponseModel(
            name=anomaly.name,
            description=anomaly.description,
            image=anomaly.image,
            media_name=anomaly.media.name, # type: ignore[attr-defined]
        )
        for anomaly in anomalies
    ]
