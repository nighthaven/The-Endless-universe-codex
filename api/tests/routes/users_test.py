from src.models.users_models import UserRole
from tests.fixtures.users_factory import UserFactory


class TestCreateUser:
    def test_create_users(self, client):
        response = client.post(
            "/users/",
            json={
                "username": "toto",
                "email": "hello123@gmail.com",
                "password": "pass",
            },
        )
        assert response.status_code == 201

    def test_create_user_email_already_exists(self, client):
        user = UserFactory(
            username="toto", email="hello123@gmail.com", password="<PASSWORD>"
        )
        response = client.post(
            "/users/",
            json={
                "username": "toto",
                "email": "hello123@gmail.com",
                "password": "<PASSWORD>",
            },
        )
        assert response.status_code == 400


class TestGetUserById:
    def test_get_user_by_email(self, client):
        user = UserFactory()
        response = client.get(f"/users/{user.email}")
        assert response.status_code == 200

    def test_get_user_not_found(self, client):
        response = client.get(f"/users/{"emailthatdoesn'texist"}")
        assert response.status_code == 404


class TestUpdateUser:
    def test_update_user_role(self, client):
        user = UserFactory()
        response = client.put(
            f"/users/{user.email}/roles", json={"roles": [UserRole.ADMIN.value]}
        )
        assert response.status_code == 200
