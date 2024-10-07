from src.serializer.user_serializer import UserResponseModel
from src.services.user_services import UserService
from src.serializer.user_serializer import UserCreationForm
from tests.factories.users_factory import UserFactory
from src.models.users_models import UserRole

class TestCreateUserService:
    def test_create_user(self, client, db_session):
        user_info = UserCreationForm(username="toto", email="hello123@gmail.com", password="pass")
        response = UserService.create_user(user_info, db_session)
        assert response.email == "hello123@gmail.com"


class TestGetUserService:
    def test_get_user(self, client, db_session):
        user = UserFactory(id="7b73a909-d93d-4ab1-a6ec-c65132ad7ec2")
        response = UserService.get_user("7b73a909-d93d-4ab1-a6ec-c65132ad7ec2", db_session)
        assert response.id == user.id
        assert response.email == user.email
        assert response.username == user.username

class TestUpdateUserService:
    def test_update_users(self, client, db_session):
        user : UserFactory = UserFactory()
        response = UserService.update_role(user.id, db_session, roles=[UserRole.ADMIN])
        assert user.roles == response.roles
        assert user.roles == [UserRole.ADMIN]



