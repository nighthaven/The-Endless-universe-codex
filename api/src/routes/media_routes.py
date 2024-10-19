from typing import Annotated, Any, List

from fastapi import APIRouter, Depends, status
from src.models.media_models import Media
from src.models.users_models import User
from src.repositories.media_repository import MediaRepository
from src.schemas.form_creation.media_form_creation import MediaFormCreation
from src.schemas.response.media_response import MediaResponse
from src.utils.Oauth2 import get_current_user

router = APIRouter(
    prefix="/media",
    tags=["media"],
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MediaResponse)
def create_media(
    media_repository: Annotated[Any, Depends(MediaRepository)],
    media: MediaFormCreation,
    current_user: User = Depends(get_current_user),
):
    new_media = Media(
        name=media.name,
        description=media.description,
    )
    new_media = media_repository.save(new_media)
    return new_media


@router.get("/", response_model=List[MediaResponse])
def get_all_media(media_repository: Annotated[Any, Depends(MediaRepository)]):
    media = media_repository.get_all()
    return media
