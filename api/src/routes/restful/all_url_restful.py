from fastapi import APIRouter, Depends
from src.services.link_service import LinkService

router = APIRouter(
    prefix="/endless",
    tags=["endless"],
)


@router.get("/")
def get_all_url():
    link_service = LinkService()
    return {
        "medias": link_service.get_restful_link("medias"),
        "factions": link_service.get_restful_link("factions"),
        "anomalies": link_service.get_restful_link("anomalies"),
        "wonders": link_service.get_restful_link("wonders"),
        "planets": link_service.get_restful_link("planets"),
    }
