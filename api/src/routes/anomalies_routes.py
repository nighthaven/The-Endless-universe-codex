import os
from typing import Annotated, Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from src.models import get_db
from src.models.anomalies_models import Anomaly
from src.models.media_models import Media, MediaName
from src.models.users_models import User
from src.serializer.anomalies_serializer import AnomalyBase, AnomalyResponseModel
from src.services.anomaly_services import AnomalyService
from src.services.media_services import MediaService
from src.utils.Oauth2 import get_current_user

router = APIRouter(
    prefix="/anomalies",
    tags=["anomalies"],
)

IMAGE_BASE_PATH = os.path.join("public", "static", "image", "endlesslegend")


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_anomaly(
    anomaly_service: Annotated[Any, Depends(AnomalyService)],
    media_service: Annotated[Any, Depends(MediaService)],
    anomalyFormCreation: AnomalyBase,
    current_user: User = Depends(get_current_user),
):
    media = media_service.get_by_name(anomalyFormCreation.media_name)
    if not media:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="media not found"
        )

    image_path = os.path.join(IMAGE_BASE_PATH, anomalyFormCreation.image)

    new_anomaly = Anomaly(
        name=anomalyFormCreation.name,
        description=anomalyFormCreation.description,
        image=image_path,
        media_id=media.id,
    )
    new_anomaly = anomaly_service.create(new_anomaly)
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
            media_name=anomaly.media.name,  # type: ignore[attr-defined]
        )
        for anomaly in anomalies
    ]
