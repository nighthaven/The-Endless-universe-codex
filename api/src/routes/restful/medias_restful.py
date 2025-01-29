from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from src.repositories.media_repository import MediaRepository

router = APIRouter(
    prefix="/endless/medias",
    tags=["medias"],
)


@router.get("/")
def list_medias(
    media_repository: MediaRepository = Depends(MediaRepository),
):
    medias_list = media_repository.get_all()
    return {
        "count": len(medias_list),
        "results": [{"name": media.name} for media in medias_list],
    }
