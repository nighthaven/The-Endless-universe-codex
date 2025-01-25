from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Query
from src.models.anomalies_models import Anomaly
from src.repositories.anomaly_repository import AnomalyRepository
from src.repositories.planet_repository import PlanetRepository

router = APIRouter(
    prefix="/endless/planets",
    tags=["planets"],
)


@router.get("/")
def list_planets(planet_repository: PlanetRepository = Depends(PlanetRepository)):
    planets_list = planet_repository.get_all()  # type: ignore[no-untyped-call]
    return {
        "count": planets_list.count(),
        "results": [
            {"name": planet.name, "url": planet.url} for planet in planets_list
        ],
    }


@router.get("/{planet_id}")
def get_planet(
    planet_id: int, planet_repository: PlanetRepository = Depends(PlanetRepository)
):
    planet = planet_repository.find_by_id(planet_id)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    return {
        "id": planet.id,
        "name": planet.name,
        "type": planet.type,
        "description": planet.description,
        "url": planet.url,
    }
