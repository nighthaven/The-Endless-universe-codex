import os

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


class TestGetAnomaly:
    def test_get_anomaly(self, client, db_session):
        anomaly = AnomalyFactory()
        AnomalyFactory()
        AnomalyFactory()
        anomaly_service = AnomalyService(db_session)
        response = anomaly_service.get_all()
        assert len(response) == 3
        assert response[0].name == anomaly.name
        assert response[0].description == anomaly.description
        assert response[0].image == anomaly.image
        assert response[0].media_id == anomaly.media_id
