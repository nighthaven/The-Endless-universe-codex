from src.models.wonders_models import Wonder
from src.repositories.wonder_repository import WonderRepository
from tests.fixtures.media_factory import MediaFactory
from tests.fixtures.wonder_factory import WonderFactory


class TestCreateWonder:
    def test_create_wonder(self, client, db_session):
        media = MediaFactory()
        wonder = Wonder(
            name="wonder_exemple",
            description="just an exemple of wonder",
            image="http://example.com/static/image/example_of_wonder.png",
            url="to_define",
            media_id=media.id,
        )
        wonder_repository = WonderRepository(db_session)
        response = wonder_repository.save(wonder)
        assert response.name == wonder.name
        assert response.description == wonder.description
        assert response.image == wonder.image
        assert response.url == wonder.url
        assert response.media_id == wonder.media_id


class TestGetWonder:
    def test_get_all_wonder(self, client, db_session):
        wonder = WonderFactory()
        wonder2 = WonderFactory()
        wonder3 = WonderFactory()
        anomaly_repository = WonderRepository(db_session)
        response = anomaly_repository.get_all()
        assert response.all() == [wonder, wonder2, wonder3]

    def test_find_by_id_anomaly(self, client, db_session):
        wonder = WonderFactory()
        anomaly_repository = WonderRepository(db_session)
        response = anomaly_repository.find_by_id(wonder.id)
        assert response.id == wonder.id
        assert response.name == wonder.name
        assert response.description == wonder.description
        assert response.image == wonder.image
        assert response.url == wonder.url
        assert response.media_id == wonder.media_id

    def test_get_wonder(self, client, db_session):
        wonder = WonderFactory()
        WonderFactory()
        WonderFactory()
        anomaly_repository = WonderRepository(db_session)
        response = anomaly_repository.find_all()
        assert len(response) == 3
        assert response[0].name == wonder.name
        assert response[0].description == wonder.description
        assert response[0].image == wonder.image
        assert response[0].url == wonder.url
        assert response[0].media_id == wonder.media_id
