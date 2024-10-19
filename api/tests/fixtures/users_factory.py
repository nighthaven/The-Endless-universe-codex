import factory
from src.models.users_models import User, UserRole
from src.utils.crypto import hash_password


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = None
        sqlalchemy_session_persistence = "commit"

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = hash_password("pass")
    created_at = factory.Faker("date_time")
    roles = [UserRole.MEMBER]
