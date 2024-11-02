from tests.fixtures.faction_description_factory import FactionDescriptionFactory


class TestGetFactionsDescriptions:
    def test_get_faction_description(self, client):
        faction_description = FactionDescriptionFactory()
        FactionDescriptionFactory()
        FactionDescriptionFactory()
        response = client.get("/factions")
        assert response.status_code == 200

        first_element_response_json = response.json()[0]
        assert first_element_response_json["faction"] == {
            "name": faction_description.faction.name
        }
        assert (
            first_element_response_json["description"]
            == faction_description.description
        )
        assert first_element_response_json["media"] == {
            "name": faction_description.media.name.value
        }
        assert first_element_response_json["image_url"] == faction_description.image_url
        assert first_element_response_json["major"] == faction_description.major
        assert (
            first_element_response_json["government"] == faction_description.government
        )
        assert first_element_response_json["ideology"] == faction_description.ideology
        assert (
            first_element_response_json["home_planet"]
            == faction_description.home_planet
        )
        assert (
            first_element_response_json["populations"]
            == faction_description.populations
        )
        assert first_element_response_json["traits"] == faction_description.traits
        assert (
            first_element_response_json["starting_technology"]
            == faction_description.starting_technology
        )
        assert first_element_response_json["units"] == faction_description.units
        assert first_element_response_json["heroes"] == faction_description.heroes
