from tests.fixtures.wonder_factory import WonderFactory


class TestGetWonderRestful:
    def test_get_wonder_restful(self, client):
        wonder = WonderFactory()
        wonder2 = WonderFactory()
        response = client.get("/endless/wonders")
        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0].get("name") == wonder.name
        assert response.json()["results"][0].get("url") == wonder.url
        assert response.json()["results"][1].get("name") == wonder2.name
        assert response.json()["results"][1].get("url") == wonder2.url

    def test_get_wonder_restful_by_id(self, client):
        wonder = WonderFactory()
        response = client.get(f"/endless/wonders/{wonder.id}")
        assert response.status_code == 200
        assert response.json().get("id") == 1
        assert response.json().get("name") == wonder.name
        assert response.json().get("description") == wonder.description
        assert response.json().get("image") == wonder.image
        assert response.json().get("url") == wonder.url
        assert response.json().get("media_id") == wonder.media_id

    def test_get_anomaly_restful_by_id_not_found(self, client):
        response = client.get(f"/endless/wonders/404")
        assert response.status_code == 404
        assert response.json() == {"detail": "Wonder not found"}
