import os

from src.services.link_service import LinkService
from tests.fixtures.media_factory import MediaFactory

IMAGE_BASE_PATH = os.path.join("public", "static", "images")


class TestLinkService:
    def test_get_image_anomalies_link(self, client, db_session):
        media = MediaFactory()
        link_service = LinkService()

        response = link_service.get_image_anomalies_link(
            media.name.name, "super-fichier-image"
        )
        assert (
            response
            == "public/static/images/ENDLESS_SPACE_2/anomalies/super-fichier-image.png"
        )

    def test_get_image_wonders_link(self, client, db_session):
        media = MediaFactory()
        link_service = LinkService()

        response = link_service.get_image_wonders_link(
            media.name.name, "super-fichier-image"
        )
        assert (
            response
            == "public/static/images/ENDLESS_SPACE_2/wonders/super-fichier-image.png"
        )

    def test_get_image_faction_description_link(self, client, db_session):
        link_service = LinkService()
        response = link_service.get_image_faction_description_link(
            "ENDLESS_LEGEND", "fakeimage", "1"
        )
        assert (
            response
            == f"{IMAGE_BASE_PATH}/ENDLESS_LEGEND/faction_description/faction-fakeimage-1.png"
        )

    def test_get_restful_link(self, client, db_session):
        link_service = LinkService()
        response = link_service.get_restful_link("test-link-name")
        assert response == "http://127.0.0.1:8000/endless/test-link-name"
