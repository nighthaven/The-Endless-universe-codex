from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, status

from src.models.media_models import Media
from src.models.users_models import User
from src.serializer.media_serializer import MediaFormCreation, MediaResponseModel
from src.services.media_services import MediaService
from src.utils.Oauth2 import get_current_user

router = APIRouter(
    prefix="/media",
    tags=["media"],
)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=MediaResponseModel
)
def create_media(
    media_service: Annotated[Any, Depends(MediaService)],
    media: MediaFormCreation,
    current_user: User = Depends(get_current_user),
):
    new_media = Media(
        name=media.name,
        description=media.description,
    )
    new_media = media_service.create(new_media)
    return new_media


@router.get("/", response_model=List[MediaResponseModel])
def get_all_media(media_service: Annotated[Any, Depends(MediaService)]):
    media = media_service.get_all()
    return media
