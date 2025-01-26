from fastapi import APIRouter, Depends, HTTPException
from src.repositories.faction_repository import FactionRepository

router = APIRouter(
    prefix="/endless/factions",
    tags=["factions"],
)


@router.get("/")
def list_factions(faction_repository: FactionRepository = Depends(FactionRepository)):
    faction_list = faction_repository.get_all()  # type: ignore[no-untyped-call]
    return {
        "count": faction_list.count(),
        "results": [
            {"name": faction.name, "url": faction.url} for faction in faction_list
        ],
    }


@router.get("/{faction_id}/")
def get_faction(
    faction_id: int, faction_repository: FactionRepository = Depends(FactionRepository)
):
    faction = faction_repository.find_by_id(faction_id)
    if not faction:
        raise HTTPException(status_code=404, detail="Faction not found")
    return {
        "id": faction.id,
        "name": faction.name,
        "url": faction.url,
    }
