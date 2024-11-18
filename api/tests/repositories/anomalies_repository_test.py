from src.models.anomalies_models import Anomaly
from src.repositories.anomaly_repository import AnomalyRepository
from tests.fixtures.anomalies_factory import AnomalyFactory
from tests.fixtures.media_factory import MediaFactory


class TestCreateAnomaly:
    def test_create_anomaly(self, client, db_session):
        media = MediaFactory()
        anomaly = Anomaly(
            name="anomaly_exemple",
            description="just an exemple of anomaly",
            image="http://example.com/static/image/example_of_anomaly",
            url="to_define",
            media_id=media.id,
        )
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.save(anomaly)
        assert response.name == anomaly.name
        assert response.description == anomaly.description
        assert response.image == anomaly.image
        assert response.url == anomaly.url
        assert response.media_id == anomaly.media_id


class TestGetAnomaly:
    def test_get_all_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        anomaly2 = AnomalyFactory()
        anomaly3 = AnomalyFactory()
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.get_all()
        assert response.all() == [anomaly, anomaly2, anomaly3]

    def test_find_by_id_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.find_by_id(anomaly.id)
        assert response.id == anomaly.id
        assert response.name == anomaly.name
        assert response.description == anomaly.description
        assert response.image == anomaly.image
        assert response.url == anomaly.url
        assert response.media_id == anomaly.media_id

    def test_anomaly_find_by(self, client, db_session):
        anomaly = AnomalyFactory()
        AnomalyFactory()
        AnomalyFactory()
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.find_by()
        assert len(response) == 3
        assert response[0].name == anomaly.name
        assert response[0].description == anomaly.description
        assert response[0].image == anomaly.image
        assert response[0].url == anomaly.url
        assert response[0].media_id == anomaly.media_id
