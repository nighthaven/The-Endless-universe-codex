from src.services.media_services import MediaServices
from tests.factories.media_factory import MediaFactory

class TestCreateMediaService:
    def test_create_media_service(self, client, db_session):
        media = MediaFactory()
        response = MediaServices.create(media, db_session)
        assert response.name == media.name
        assert response.description == media.description

    def test_get_all_media_services(self, client, db_session):
        media1 = MediaFactory()
        media2 = MediaFactory()
        media3 = MediaFactory()
        response = MediaServices.get_all(db_session)
        assert len(response) == 3
        assert response[0].name == media1.name
        assert response[1].name == media2.name
        assert response[2].name == media3.name
        assert response[0].description == media1.description
        assert response[1].description == media2.description
        assert response[2].description == media3.description