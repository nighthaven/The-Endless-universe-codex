from typing import Annotated, Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from src.enums.media_name import MediaName
from src.models.users_models import User
from src.models.wonders_models import Wonder
from src.repositories.media_repository import MediaRepository
from src.repositories.wonder_repository import WonderRepository
from src.schemas.form_creation.wonder_form_creation import WonderFormCreation
from src.schemas.response.wonders_response import WonderResponseModel
from src.services.link_service import LinkService
from src.utils.Oauth2 import get_current_user

router = APIRouter(
    prefix="/wonders",
    tags=["wonders"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def create_wonder(
    wonder_repository: Annotated[Any, Depends(WonderRepository)],
    link_service: Annotated[LinkService, Depends(LinkService)],
    media_repository: Annotated[Any, Depends(MediaRepository)],
    wonder_form_creation: WonderFormCreation,
    current_user: User = Depends(get_current_user),
):
    media = media_repository.get_by_name(wonder_form_creation.media_name)
    if not media:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="media not found"
        )
    image_path = link_service.get_image_wonders_link(
        media.name.name, wonder_form_creation.image
    )
    new_wonder = Wonder(
        name=wonder_form_creation.name,
        description=wonder_form_creation.description,
        image=image_path,
        url="to_define",
        media_id=media.id,
    )
    new_wonder = wonder_repository.save(new_wonder)
    new_wonder.url = link_service.get_restful_link(f"wonder/{new_wonder.id}")
    new_wonder = wonder_repository.update(new_wonder)
    return new_wonder


@router.get("/", response_model=List[WonderResponseModel])
def get_all_wonders(
    wonder_repository: WonderRepository = Depends(WonderRepository),
    media: Optional[MediaName] = None,
    wonder_name: Optional[str] = None,
) -> List[WonderResponseModel]:
    wonder_query = wonder_repository.find_all(media, wonder_name)
    return [
        WonderResponseModel(
            name=wonder.name,
            description=wonder.description,
            image=wonder.image,
            media_name=wonder.media.name,
        )
        for wonder in wonder_query
    ]
