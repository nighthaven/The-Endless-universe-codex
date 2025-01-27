import factory
from src.models.faction_description_model import FactionDescription
from tests.fixtures.factions_factory import FactionFactory
from tests.fixtures.media_factory import MediaFactory
from tests.fixtures.planet_factory import PlanetFactory


class FactionDescriptionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = FactionDescription
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    faction_id = factory.LazyAttribute(lambda obj: FactionFactory().id)
    media_id = factory.LazyAttribute(lambda obj: MediaFactory().id)
    description = factory.Faker("text")
    image_url = factory.LazyAttribute(
        lambda _: f"http://example.com/images/default_image.png"
    )
    government = factory.Sequence(lambda n: f"government {n}")
    ideology = factory.Sequence(lambda n: f"ideology {n}")
    home_planet = factory.SubFactory(PlanetFactory)
    affinity = factory.List(["affinity1", "affinity2", "affinity3"])
    populations = factory.List(["humain", "elfe", "nain"])
    traits = factory.List(["trait1", "trait2", "trait3"])
    starting_technology = factory.List(["tech1", "tech2", "tech3"])
    units = factory.List(["unit1", "unit2", "unit3"])
    heroes = factory.List(["hero1", "hero2", "hero3"])
    major = factory.Faker("boolean")
    url = factory.Sequence(
        lambda n: f"http://example.com/endless/faction-descriptions/{n}"
    )
