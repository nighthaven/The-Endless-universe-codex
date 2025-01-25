from tests.fixtures.factions_factory import FactionFactory


class TestGetFactionRestful:
    def test_get_factions_restful(self, client):
        faction = FactionFactory()
        faction2 = FactionFactory()
        response = client.get("/endless/factions")
        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0].get("name") == faction.name
        assert response.json()["results"][0].get("url") == faction.url
        assert response.json()["results"][1].get("name") == faction2.name
        assert response.json()["results"][1].get("url") == faction2.url

    def test_get_faction_restful_by_id(self, client):
        faction = FactionFactory()
        response = client.get(f"/endless/factions/{faction.id}")
        assert response.status_code == 200
        assert response.json().get("id") == faction.id
        assert response.json().get("name") == faction.name
        assert response.json().get("url") == faction.url

    def test_get_anomaly_restful_by_id_not_found(self, client):
        response = client.get(f"/endless/anomalies/404")
        assert response.status_code == 404
        assert response.json() == {"detail": "Anomaly not found"}
