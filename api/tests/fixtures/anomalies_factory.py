import factory
from src.models.anomalies_models import Anomaly
from tests.fixtures.media_factory import MediaFactory


class AnomalyFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Anomaly
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    name = factory.Sequence(lambda n: f"Anomaly {n}")
    description = factory.Faker("text")
    image = factory.LazyAttribute(
        lambda _: f"http://example.com/images/{_.name.replace(' ', '_')}.png"
    )
    media_id = factory.LazyAttribute(lambda obj: MediaFactory().id)
