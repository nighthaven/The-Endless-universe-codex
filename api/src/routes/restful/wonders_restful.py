from fastapi import APIRouter, Depends, HTTPException
from src.repositories.wonder_repository import WonderRepository

router = APIRouter(
    prefix="/endless/wonders",
    tags=["wonders"],
)


@router.get("/")
def list_wonders(
    wonder_repository: WonderRepository = Depends(WonderRepository),
):
    wonders_list = wonder_repository.get_all()  # type: ignore[no-untyped-call]
    return {
        "count": wonders_list.count(),
        "results": [
            {"name": wonder.name, "url": wonder.url} for wonder in wonders_list
        ],
    }


@router.get("/{wonder_id}/")
def get_wonder(
    wonder_id: int, wonder_repository: WonderRepository = Depends(WonderRepository)
):
    wonder = wonder_repository.find_by_id(wonder_id)
    if not wonder:
        raise HTTPException(status_code=404, detail="Wonder not found")
    return {
        "id": wonder.id,
        "name": wonder.name,
        "description": wonder.description,
        "image": wonder.image,
        "url": wonder.url,
        "media_id": wonder.media_id,
        "media": wonder.media.name,  # type: ignore[attr-defined]
    }
