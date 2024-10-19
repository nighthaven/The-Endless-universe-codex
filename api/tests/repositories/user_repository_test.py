from src.models.users_models import User, UserRole
from src.repositories.user_repository import UserRepository
from tests.fixtures.users_factory import UserFactory


class TestCreateUserRepository:
    def test_create_user(self, client, db_session):
        user_info = User(username="toto", email="hello123@gmail.com", password="pass")
        user_repository = UserRepository(db_session)
        response = user_repository.save_user(user_info)
        assert response.email == "hello123@gmail.com"


class TestGetUserRepository:
    def test_get_user(self, client, db_session):
        user = UserFactory()
        user_repository = UserRepository(db_session)
        response = user_repository.get_user_by_email(user.email)
        assert response.id == user.id
        assert response.email == user.email
        assert response.username == user.username


class TestUpdateUserRepository:
    def test_update_users(self, client, db_session):
        user: UserFactory = UserFactory()
        user_repository = UserRepository(db_session)
        response = user_repository.update_role(email=user.email, roles=[UserRole.ADMIN])
        assert user.roles == response.roles
        assert user.roles == [UserRole.ADMIN]
