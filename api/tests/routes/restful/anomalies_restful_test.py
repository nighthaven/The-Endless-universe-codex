from tests.fixtures.anomalies_factory import AnomalyFactory


class TestGetAnomalyRestful:
    def test_get_anomaly_restful(self, client):
        anomaly = AnomalyFactory()
        anomaly2 = AnomalyFactory()
        response = client.get("/endless/anomalies")
        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0].get("name") == anomaly.name
        assert response.json()["results"][0].get("url") == anomaly.url
        assert response.json()["results"][1].get("name") == anomaly2.name
        assert response.json()["results"][1].get("url") == anomaly2.url

    def test_get_anomaly_restful_by_id(self, client):
        anomaly = AnomalyFactory()
        response = client.get(f"/endless/anomalies/{anomaly.id}")
        assert response.status_code == 200
        assert response.json().get("id") == 1
        assert response.json().get("name") == anomaly.name
        assert response.json().get("description") == anomaly.description
        assert response.json().get("image") == anomaly.image
        assert response.json().get("url") == anomaly.url
        assert response.json().get("media_id") == anomaly.media_id

    def test_get_anomaly_restful_by_id_not_found(self, client):
        response = client.get(f"/endless/anomalies/404")
        assert response.status_code == 404
        assert response.json() == {"detail": "Anomaly not found"}
