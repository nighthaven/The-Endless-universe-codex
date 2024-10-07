import uuid

from src.models.users_models import UserRole
from tests.factories.users_factory import UserFactory


class TestCreateUser:
    def test_create_users(self, client):
        response = client.post("/users/", json={"username": "toto", "email": "hello123@gmail.com", "password": "pass"})
        assert response.status_code == 201

    def test_create_user_email_already_exists(self, client):
        user = UserFactory(username="toto", email="hello123@gmail.com", password="<PASSWORD>")
        response = client.post("/users/", json={"username": "toto", "email": "hello123@gmail.com", "password": "<PASSWORD>"})
        assert response.status_code == 400


class TestGetUserById:
    def test_get_user_by_id(self, client):
        user = UserFactory(id="7b73a909-d93d-4ab1-a6ec-c65132ad7ec2")
        response = client.get(f"/users/{user.id}")
        assert response.status_code == 200

    def test_get_user_not_found(self, client):
        response = client.get(f"/users/{uuid.uuid4()}")
        assert response.status_code == 404


class TestUpdateUser:
    def test_update_user_role(self, client):
        user = UserFactory()
        response = client.put(f"/users/{user.id}/roles", json={"roles": [UserRole.ADMIN.value]})
        assert response.status_code == 200


