from src.repositories.media_repository import MediaRepository
from tests.fixtures.media_factory import MediaFactory


class TestCreateMediaRepository:
    def test_create_media_repository(self, client, db_session):
        media = MediaFactory()
        media_repository = MediaRepository(db_session)
        response = media_repository.save(media)
        assert response.name == media.name
        assert response.description == media.description


class TestGetMediaRepository:
    def test_get_all_media(self, client, db_session):
        media = MediaFactory()
        media2 = MediaFactory()
        media3 = MediaFactory()
        media_repository = MediaRepository(db_session)
        response = media_repository.get_all()
        assert response == [media, media2, media3]

    def test_get_all_media_repository(self, client, db_session):
        media_1 = MediaFactory()
        media_2 = MediaFactory()
        media_3 = MediaFactory()
        media_repository = MediaRepository(db_session)
        response = media_repository.get_all()
        assert len(response) == 3
        assert response[0].name == media_1.name
        assert response[1].name == media_2.name
        assert response[2].name == media_3.name
        assert response[0].description == media_1.description
        assert response[1].description == media_2.description
        assert response[2].description == media_3.description
