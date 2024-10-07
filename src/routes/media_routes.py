from fastapi import APIRouter, status, Depends
from typing import Annotated, List, Any
from sqlalchemy.orm import Session

from src.models import get_db
from src.models.users_models import User
from src.serializer.media_serializer import MediaResponseModel, MediaFormCreation
from src.utils.Oauth2 import get_current_user
from src.services.media_services import MediaService


router = APIRouter(
    prefix="/media",
    tags=["media"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MediaResponseModel)
def create_media(media: MediaFormCreation, db: Annotated[Session, Depends(get_db)], current_user: User = Depends(get_current_user)):
    new_media = MediaService.create(media, db)
    return new_media


@router.get("/", response_model=List[MediaResponseModel])
def get_all_media(media_service: Annotated[Any, Depends(MediaService)]):
    media = media_service.get_all()
    return media


