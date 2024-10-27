import os

from src.models.media_models import MediaName
from tests.fixtures.anomalies_factory import AnomalyFactory
from tests.fixtures.media_factory import MediaFactory

IMAGE_BASE_PATH = os.path.join(
    "public", "static", "images", "ENDLESS_SPACE_2", "anomalies"
)


class TestCreateAnomaly:
    def test_create_anomaly(self, authenticated_client):
        media = MediaFactory()
        anomaly = {
            "name": "anomalie anormale",
            "description": "une très étrange anomalie que voila",
            "image": "Anomalies-Endless-L-1",
            "media_name": media.name.value,
        }

        response = authenticated_client.post("/anomalies", json=anomaly)
        assert response.status_code == 201
        assert response.json()["name"] == anomaly["name"]
        assert response.json()["description"] == anomaly["description"]
        assert response.json()["image"] == os.path.join(
            IMAGE_BASE_PATH, f"{anomaly["image"]}.png"
        )
        assert response.json()["media_id"] == media.id

    def test_create_anomaly_with_unknown_client(self, client):
        media = MediaFactory()
        anomaly = {
            "name": "anomalie anormale",
            "description": "une très étrange anomalie que voila",
            "image": "Anomalies-Endless L-1.png",
            "media_name": media.name.value,
        }
        response = client.post("/anomalies", json=anomaly)
        assert response.status_code == 401


class TestGetAnomaly:
    def test_get_anomaly(self, client):
        anomaly = AnomalyFactory()
        anomaly2 = AnomalyFactory()
        response = client.get("/anomalies")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == anomaly.name
        assert response.json()[0]["description"] == anomaly.description
        assert response.json()[0]["image"] == anomaly.image
        assert response.json()[0]["media_name"] == anomaly.media.name.value
        assert response.json()[1]["name"] == anomaly2.name
        assert response.json()[1]["description"] == anomaly2.description
        assert response.json()[1]["image"] == anomaly2.image
        assert response.json()[1]["media_name"] == anomaly2.media.name.value

    def test_get_anomaly_search_by_name(self, client):
        AnomalyFactory()
        anomaly2 = AnomalyFactory(name="The one searched")
        AnomalyFactory()
        response = client.get("/anomalies", params={"anomaly_name": "The one searched"})
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == anomaly2.name
        assert response.json()[0]["description"] == anomaly2.description
        assert response.json()[0]["image"] == anomaly2.image
        assert response.json()[0]["media_name"] == anomaly2.media.name.value

    def test_get_anomaly_search_by_media(self, client):
        AnomalyFactory()
        AnomalyFactory()
        media = MediaFactory(name=MediaName.ENDLESS_LEGEND)
        anomalie_3 = AnomalyFactory(media_id=media.id)
        response = client.get("/anomalies", params={"media": "Endless Legend"})
        assert response.status_code == 200
        assert response.json()[0]["name"] == anomalie_3.name
        assert response.json()[0]["description"] == anomalie_3.description
        assert response.json()[0]["image"] == anomalie_3.image
        assert response.json()[0]["media_name"] == anomalie_3.media.name.value
