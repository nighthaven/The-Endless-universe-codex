from src.enums.media_name import MediaName
from tests.fixtures.faction_description_factory import FactionDescriptionFactory
from src.repositories.faction_repository import FactionDescriptionRepository
from tests.fixtures.factions_factory import FactionFactory
from tests.fixtures.media_factory import MediaFactory


class TestGetFactionDescription:
    def test_get_faction_description(self, client, db_session):
        faction = FactionDescriptionFactory()
        FactionDescriptionFactory()
        FactionDescriptionFactory()
        faction_repository = FactionDescriptionRepository(db_session)
        response = faction_repository.find_by()
        assert len(response) == 3
        assert response[0].faction_id == faction.faction_id
        assert response[0].media_id == faction.media_id
        assert response[0].description == faction.description
        assert response[0].affinity == faction.affinity
        assert response[0].government == faction.government
        assert response[0].home_planet == faction.home_planet
        assert response[0].units == faction.units
        assert response[0].heroes == faction.heroes
        assert response[0].major == faction.major
        assert response[0].ideology == faction.ideology

    def test_get_faction_description_specific_media(self, client, db_session):
        media = MediaFactory(name=MediaName.ENDLESS_LEGEND)
        FactionDescriptionFactory(media_id=media.id)
        FactionDescriptionFactory()
        FactionDescriptionFactory()
        faction_repository = FactionDescriptionRepository(db_session)
        response = faction_repository.find_by(media=MediaName.ENDLESS_LEGEND)
        assert len(response) == 1
        assert response[0].media.name == media.name


    def test_get_faction_description_specific_faction(self, client, db_session):
        fac = FactionFactory(name="Amplitude")
        FactionDescriptionFactory(faction_id=fac.id)
        FactionDescriptionFactory()
        FactionDescriptionFactory()
        faction_repository = FactionDescriptionRepository(db_session)
        response = faction_repository.find_by(faction_name="Amplitude")
        assert len(response) == 1
        assert response[0].faction.name == fac.name
