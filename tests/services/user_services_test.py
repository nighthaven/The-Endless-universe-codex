from src.models.users_models import User, UserRole
from src.services.user_services import UserService
from tests.factories.users_factory import UserFactory


class TestCreateUserService:
    def test_create_user(self, client, db_session):
        user_info = User(username="toto", email="hello123@gmail.com", password="pass")
        user_service = UserService(db_session)
        response = user_service.create_user(user_info)
        assert response.email == "hello123@gmail.com"


class TestGetUserService:
    def test_get_user(self, client, db_session):
        user = UserFactory()
        user_service = UserService(db_session)
        response = user_service.get_user_by_email(user.email)
        assert response.id == user.id
        assert response.email == user.email
        assert response.username == user.username


class TestUpdateUserService:
    def test_update_users(self, client, db_session):
        user: UserFactory = UserFactory()
        user_service = UserService(db_session)
        response = user_service.update_role(email=user.email, roles=[UserRole.ADMIN])
        assert user.roles == response.roles
        assert user.roles == [UserRole.ADMIN]
