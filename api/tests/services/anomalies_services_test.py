from src.services.link_service import LinkService
from tests.fixtures.media_factory import MediaFactory


class TestLinkService:
    def test_get_image_anomalies_link(self, client, db_session):
        media = MediaFactory()
        link_service = LinkService()

        response = link_service.get_image_anomalies_link(
            media.name.name, "super-fichier-image"
        )
        assert (
            response
            == "public/static/image/ENDLESS_SPACE_2/anomalies/super-fichier-image.png"
        )

    def test_get_image_wonders_link(self, client, db_session):
        media = MediaFactory()
        link_service = LinkService()

        response = link_service.get_image_wonders_link(
            media.name.name, "super-fichier-image"
        )
        assert (
            response
            == "public/static/image/ENDLESS_SPACE_2/wonders/super-fichier-image.png"
        )
