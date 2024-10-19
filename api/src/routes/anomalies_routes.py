from typing import Annotated, Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from src.enums.media_name import MediaName
from src.models.anomalies_models import Anomaly
from src.models.users_models import User
from src.repositories.anomaly_repository import AnomalyRepository
from src.repositories.media_repository import MediaRepository
from src.schemas.form_creation.anomaly_form_creation import AnomalyFormCreation
from src.schemas.response.anomalies_response import AnomalyResponse
from src.services.link_service import LinkService
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
    anomaly_repository: Annotated[Any, Depends(AnomalyRepository)],
    link_service: Annotated[LinkService, Depends(LinkService)],
    media_repository: Annotated[Any, Depends(MediaRepository)],
    anomaly_form_creation: AnomalyFormCreation,
    current_user: User = Depends(get_current_user),
):
    media = media_repository.get_by_name(anomaly_form_creation.media_name)
    if not media:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="media not found"
        )

    image_path = link_service.get_image_anomalies_link(
        media.name.name, anomaly_form_creation.image
    )
    new_anomaly = Anomaly(
        name=anomaly_form_creation.name,
        description=anomaly_form_creation.description,
        image=image_path,
        media_id=media.id,
    )
    new_anomaly = anomaly_repository.save(new_anomaly)
    return new_anomaly


@router.get("/", response_model=List[AnomalyResponse])
def get_all_anomalies(
    anomaly_repository: AnomalyRepository = Depends(AnomalyRepository),
    media: Optional[MediaName] = None,
    anomaly_name: Optional[str] = None,
) -> List[AnomalyResponse]:
    anomaly_query = anomaly_repository.find_by(media, anomaly_name)
    return [
        AnomalyResponse(
            name=anomaly.name,
            description=anomaly.description,
            image=anomaly.image,
            media_name=anomaly.media.name,
        )
        for anomaly in anomaly_query
    ]
