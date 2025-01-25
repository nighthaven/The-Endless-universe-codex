import os

from src.models.media_models import MediaName
from tests.fixtures.media_factory import MediaFactory
from tests.fixtures.wonder_factory import WonderFactory

IMAGE_BASE_PATH = os.path.join(
    "public", "static", "images", "ENDLESS_SPACE_2", "wonders"
)


class TestCreateWonder:
    def test_create_wonder(self, authenticated_client):
        media = MediaFactory()
        wonder = {
            "name": "merveille sublime",
            "description": "une sublime merveille que voila",
            "image": "Wonder-Endless-L-1",
            "url": "http://127.0.0.1:8000/endless/wonder/1",
            "media_name": media.name.value,
        }

        response = authenticated_client.post("/wonders", json=wonder)
        assert response.status_code == 201
        assert response.json()["name"] == wonder["name"]
        assert response.json()["description"] == wonder["description"]
        assert response.json()["image"] == os.path.join(
            IMAGE_BASE_PATH, f"{wonder["image"]}.png"
        )
        assert response.json()["url"] == wonder["url"]
        assert response.json()["media_id"] == media.id

    def test_create_wonder_with_unknown_client(self, client):
        media = MediaFactory()
        wonder = {
            "name": "merveille sublime",
            "description": "une sublime merveille que voila",
            "image": "Wonder-Endless L-1.png",
            "media_name": media.name.value,
        }
        response = client.post("/wonders", json=wonder)
        assert response.status_code == 401


class TestGetwonders:
    def test_get_wonders(self, client):
        wonder = WonderFactory()
        wonder_2 = WonderFactory()
        response = client.get("/wonders")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["name"] == wonder.name
        assert response.json()[0]["description"] == wonder.description
        assert response.json()[0]["image"] == wonder.image
        assert response.json()[0]["media_name"] == wonder.media.name.value
        assert response.json()[1]["name"] == wonder_2.name
        assert response.json()[1]["description"] == wonder_2.description
        assert response.json()[1]["image"] == wonder_2.image
        assert response.json()[1]["media_name"] == wonder_2.media.name.value

    def test_get_wonder_search_by_name(self, client):
        WonderFactory()
        wonder_2 = WonderFactory(name="The one searched")
        WonderFactory()
        response = client.get("/wonders", params={"wonder_name": "The one searched"})
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["name"] == wonder_2.name
        assert response.json()[0]["description"] == wonder_2.description
        assert response.json()[0]["image"] == wonder_2.image
        assert response.json()[0]["media_name"] == wonder_2.media.name.value

    def test_get_anomaly_search_by_media(self, client):
        WonderFactory()
        WonderFactory()
        media = MediaFactory(name=MediaName.ENDLESS_LEGEND)
        wonder_3 = WonderFactory(media_id=media.id)
        response = client.get("/wonders", params={"media": "Endless Legend"})
        assert response.status_code == 200
        assert response.json()[0]["name"] == wonder_3.name
        assert response.json()[0]["description"] == wonder_3.description
        assert response.json()[0]["image"] == wonder_3.image
        assert response.json()[0]["media_name"] == wonder_3.media.name.value
