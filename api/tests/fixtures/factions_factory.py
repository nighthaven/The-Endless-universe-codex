import factory
from src.models.factions_models import Faction


class FactionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Faction
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    name = factory.Sequence(lambda n: f"Faction {n}")
    url = factory.Sequence(lambda n: f"http://example.com/endless/factions/{n}")
