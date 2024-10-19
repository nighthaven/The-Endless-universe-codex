import factory
from src.models.wonders_models import Wonder
from tests.fixtures.media_factory import MediaFactory


class WonderFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Wonder
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    name = factory.Sequence(lambda n: f"Wonder {n}")
    description = factory.Faker("text")
    image = factory.LazyAttribute(
        lambda _: f"http://example.com/images/{_.name.replace(' ', '_')}.png"
    )
    media_id = factory.LazyAttribute(lambda obj: MediaFactory().id)
