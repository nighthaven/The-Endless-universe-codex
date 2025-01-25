from tests.fixtures.planet_factory import PlanetFactory


class TestGetPlanetRestfull:
    def test_get_planets_restful(self, client):
        planet = PlanetFactory()
        planet1 = PlanetFactory()
        response = client.get("/endless/planets")
        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0].get("name") == planet.name
        assert response.json()["results"][0].get("url") == planet.url
        assert response.json()["results"][1].get("name") == planet1.name
        assert response.json()["results"][1].get("url") == planet1.url

    def test_get_planet_restful_by_id(self, client):
        planet = PlanetFactory()
        response = client.get(f"/endless/planets/{planet.id}")
        assert response.status_code == 200
        assert response.json().get("id") == 1
        assert response.json().get("name") == planet.name
        assert response.json().get("description") == planet.description
        assert response.json().get("url") == planet.url

    def test_get_planet_restful_by_id_not_found(self, client):
        response = client.get(f"/endless/planets/404")
        assert response.status_code == 404
        assert response.json() == {"detail": "Planet not found"}
