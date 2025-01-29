from fastapi import APIRouter, Depends, HTTPException
from src.repositories.faction_description_repository import FactionDescriptionRepository

router = APIRouter(
    prefix="/endless/faction-descriptions",
    tags=["faction-descriptions"],
)


@router.get("/")
def list_faction_descriptions(
    faction_descriptions_repository: FactionDescriptionRepository = Depends(
        FactionDescriptionRepository
    ),
):
    faction_descriptions_list = faction_descriptions_repository.get_all()  # type: ignore[no-untyped-call]
    return {
        "count": faction_descriptions_list.count(),
        "results": [
            {"faction name": faction.faction.name, "url": faction.url}
            for faction in faction_descriptions_list
        ],
    }


@router.get("/{faction_description_id}/")
def get_faction(
    faction_description_id: int,
    faction_descriptions_repository: FactionDescriptionRepository = Depends(
        FactionDescriptionRepository
    ),
):
    faction_description = faction_descriptions_repository.find_by_id(
        faction_description_id
    )
    if not faction_description:
        raise HTTPException(status_code=404, detail="Description not found")
    return {
        "id": faction_description.id,
        "faction name": faction_description.faction.name,
        "url": faction_description.url,
        "description": faction_description.description,
        "government": faction_description.government,
        "ideology": faction_description.ideology,
        "affinity": faction_description.affinity,
        "populations": faction_description.populations,
        "traits": faction_description.traits,
        "starting_technology": faction_description.starting_technology,
        "units": faction_description.units,
        "heroes": faction_description.heroes,
        "major": faction_description.major,
        "faction_id": faction_description.faction_id,
        "media_id": faction_description.media_id,
        "media name": faction_description.media.name,  # type: ignore[attr-defined]
        "home_planet_id": (
            faction_description.home_planet_id
            if faction_description.home_planet_id
            else None
        ),
        "home_planet": (
            faction_description.home_planet.name
            if faction_description.home_planet
            else None
        ),
    }
