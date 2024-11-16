import factory
from src.models.planets_model import Planet


class PlanetFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Planet
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    name = factory.Sequence(lambda n: f"Planet {n}")
    type = factory.Sequence(lambda n: f"Planet type {n}")
    description = factory.Faker("text")
