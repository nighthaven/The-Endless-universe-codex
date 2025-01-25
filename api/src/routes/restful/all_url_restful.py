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
        "anomalies": link_service.get_restful_link("anomalies"),
        "wonders": LinkService().get_restful_link("wonders"),
        "planets": LinkService().get_restful_link("planets"),
    }
