from fastapi import APIRouter, status, HTTPException, Depends
from typing import Annotated, List
from sqlalchemy.orm import Session

from src.models import get_db
from src.models.users_models import User
from src.models.media_models import Media
from src.serializer.media_serializer import MediaResponseModel, MediaFormCreation
from src.utils.Oauth2 import get_current_user
from src.services.media_services import MediaServices


router = APIRouter(
    prefix="/media",
    tags=["media"],
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MediaResponseModel)
def create_media(media: MediaFormCreation, db: Annotated[Session, Depends(get_db)], current_user: User = Depends(get_current_user)):
    new_media = MediaServices.create(media, db)
    return new_media


@router.get("/", response_model=List[MediaResponseModel])
def get_all_media(db: Annotated[Session, Depends(get_db)]):
    media = MediaServices.get_all(db)
    return media


