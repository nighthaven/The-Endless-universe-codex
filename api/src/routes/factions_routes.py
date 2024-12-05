from typing import Annotated, Any, List

from fastapi import APIRouter, Depends
from src.repositories.faction_repository import FactionDescriptionRepository
from src.schemas.base.faction_base import FactionResponse, MediaResponse
from src.schemas.response.faction_description_response import FactionDescriptionResponse
from src.services.link_service import LinkService

router = APIRouter(
    prefix="/factions",
    tags=["factions"],
)


@router.get("/", response_model=List[FactionDescriptionResponse])
def get_all_factions(
    faction_repository: Annotated[Any, Depends(FactionDescriptionRepository)]
):
    list_factions = faction_repository.find_by()
    return [
        FactionDescriptionResponse(
            id=faction_description.id,
            faction=FactionResponse(name=faction_description.faction.name),
            media=MediaResponse(name=faction_description.media.name),
            description=faction_description.description,
            image_url=faction_description.image_url,
            government=faction_description.government,
            ideology=faction_description.ideology,
            home_planet=faction_description.home_planet,
            affinity=faction_description.affinity,
            populations=faction_description.populations,
            traits=faction_description.traits,
            starting_technology=faction_description.starting_technology,
            units=faction_description.units,
            heroes=faction_description.heroes,
            major=faction_description.major,
            url=LinkService().get_factions_link("router", faction_description.id),
        )
        for faction_description in list_factions
    ]
