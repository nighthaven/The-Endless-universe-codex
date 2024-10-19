from src.repositories.anomaly_repository import AnomalyRepository
from tests.fixtures.anomalies_factory import AnomalyFactory


class TestCreateAnomaly:
    def test_create_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.save(anomaly)
        assert response.name == anomaly.name
        assert response.description == anomaly.description
        assert response.image == anomaly.image
        assert response.media_id == anomaly.media_id


class TestGetAnomaly:
    def test_get_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        AnomalyFactory()
        AnomalyFactory()
        anomaly_repository = AnomalyRepository(db_session)
        response = anomaly_repository.find_by()
        assert len(response) == 3
        assert response[0].name == anomaly.name
        assert response[0].description == anomaly.description
        assert response[0].image == anomaly.image
        assert response[0].media_id == anomaly.media_id
