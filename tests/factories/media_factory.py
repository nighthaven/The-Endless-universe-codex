import factory

from src.models.media_models import Media, MediaName


class MediaFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Media
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    name = MediaName.ENDLESS_SPACE_2
    description = factory.Faker("text")
