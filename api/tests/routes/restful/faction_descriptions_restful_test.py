from tests.fixtures.faction_description_factory import FactionDescriptionFactory
from tests.fixtures.factions_factory import FactionFactory


class TestGetFactionDescriptionRestful:
    def test_get_factions_descriptions_restful(self, client):
        faction = FactionDescriptionFactory()
        faction2 = FactionDescriptionFactory()

        response = client.get("/endless/faction-descriptions")

        assert response.status_code == 200
        assert response.json()["count"] == 2
        assert response.json()["results"][0].get("faction name") == faction.faction.name
        assert response.json()["results"][0].get("url") == faction.url
        assert (
            response.json()["results"][1].get("faction name") == faction2.faction.name
        )
        assert response.json()["results"][1].get("url") == faction2.url

    def test_get_faction_descriptions_restful_by_id(self, client):
        faction = FactionDescriptionFactory()

        response = client.get(f"/endless/faction-descriptions/{faction.id}")

        assert response.status_code == 200
        assert response.json().get("id") == faction.id
        assert response.json().get("faction name") == faction.faction.name
        assert response.json().get("url") == faction.url
        assert response.json().get("description") == faction.description
        assert response.json().get("government") == faction.government
        assert response.json().get("ideology") == faction.ideology
        assert response.json().get("affinity") == faction.affinity
        assert response.json().get("populations") == faction.populations
        assert response.json().get("traits") == faction.traits
        assert response.json().get("starting_technology") == faction.starting_technology
        assert response.json().get("units") == faction.units
        assert response.json().get("heroes") == faction.heroes
        assert response.json().get("major") == faction.major
        assert response.json().get("faction_id") == faction.faction_id
        assert response.json().get("media_id") == faction.media.id
        assert response.json().get("media name") == faction.media.name.value
        assert response.json().get("home_planet_id") == faction.home_planet.id
        assert response.json().get("home_planet") == faction.home_planet.name

    def test_get_faction_descriptions_restful_by_id_not_found(self, client):
        response = client.get(f"/endless/faction-descriptions/404")

        assert response.status_code == 404
        assert response.json() == {"detail": "Description not found"}
