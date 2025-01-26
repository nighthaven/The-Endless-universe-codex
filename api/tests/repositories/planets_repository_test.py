from src.models.planets_model import Planet
from src.repositories.planet_repository import PlanetRepository
from tests.fixtures.planet_factory import PlanetFactory


class TestPlanetRepository:
    def test_save_planet(self, client, db_session):
        planet = Planet(
            name="planet_exemple",
            description="just an exemple of planet",
            url="to_define",
        )

        planet_repository = PlanetRepository(db_session)
        response = planet_repository.save(planet)

        assert response.name == planet.name
        assert response.type == planet.type
        assert response.description == planet.description
        assert response.url == planet.url

    def test_get_all_planets(self, client, db_session):
        planet = PlanetFactory()
        planet2 = PlanetFactory()
        planet3 = PlanetFactory()

        planet_repository = PlanetRepository(db_session)
        response = planet_repository.get_all()

        assert response.all() == [planet, planet2, planet3]

    def test_find_by_id_planet(self, client, db_session):
        planet = PlanetFactory()

        planet_repository = PlanetRepository(db_session)
        response = planet_repository.find_by_id(planet.id)

        assert response.id == planet.id
        assert response.name == planet.name
        assert response.type == planet.type
        assert response.description == planet.description
        assert response.url == planet.url
