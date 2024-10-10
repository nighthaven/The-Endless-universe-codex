from src.services.media_services import MediaService
from tests.factories.media_factory import MediaFactory


class TestCreateMediaService:
    def test_create_media_service(self, client, db_session):
        media = MediaFactory()
        media_service = MediaService(db_session)
        response = media_service.create(media)
        assert response.name == media.name
        assert response.description == media.description

    def test_get_all_media_services(self, client, db_session):
        media_1 = MediaFactory()
        media_2 = MediaFactory()
        media_3 = MediaFactory()
        media_service = MediaService(db_session)
        response = media_service.get_all()
        assert len(response) == 3
        assert response[0].name == media_1.name
        assert response[1].name == media_2.name
        assert response[2].name == media_3.name
        assert response[0].description == media_1.description
        assert response[1].description == media_2.description
        assert response[2].description == media_3.description
