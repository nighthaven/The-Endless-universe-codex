from src.repositories.wonder_repository import WonderRepository
from tests.fixtures.wonder_factory import WonderFactory


class TestCreateWonder:
    def test_create_wonder(self, client, db_session):
        wonder = WonderFactory()
        wonder_repository = WonderRepository(db_session)
        response = wonder_repository.save(wonder)
        assert response.name == wonder.name
        assert response.description == wonder.description
        assert response.image == wonder.image
        assert response.media_id == wonder.media_id


class TestGetWonder:
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
        assert response[0].media_id == wonder.media_id
