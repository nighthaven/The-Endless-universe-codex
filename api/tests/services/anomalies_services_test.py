from src.services.anomaly_services import AnomalyService
from tests.factories.anomalies_factory import AnomalyFactory


class TestCreateAnomaly:
    def test_create_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        anomaly_service = AnomalyService(db_session)
        response = anomaly_service.create(anomaly)
        assert response.name == anomaly.name
        assert response.description == anomaly.description
        assert response.image == anomaly.image
        assert response.media_id == anomaly.media_id
