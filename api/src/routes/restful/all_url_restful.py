from fastapi import APIRouter, Depends
from src.services.link_service import LinkService

router = APIRouter(
    prefix="/endless",
    tags=["endless"],
)


@router.get("/")
def get_all_url():
    return {
        "anomalies": LinkService().get_restful_link("anomalies"),
        "wonders": LinkService().get_restful_link("wonders"),
    }
