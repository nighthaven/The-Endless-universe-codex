import pytest
import uuid

from src.serializer.user_serializer import UserResponseModel, TokenResponse
from src.utils.Oauth2 import SECRET_KEY, ALGORYTHM
from tests.factories.users_factory import UserFactory
from jose import jwt



def test_create_users(client):
    response = client.post("/users/", json={"username": "toto", "email": "hello123@gmail.com", "password": "pass"})
    assert response.status_code == 201
    new_user = UserResponseModel(**response.json())
    assert new_user.email == "hello123@gmail.com"


def test_login_user(client):
    user = UserFactory(email="test@example.com")

    response = client.post(
        "/login", data={"username": user.email, "password": "pass"}
    )

    assert response.status_code == 200
    login_response = TokenResponse(**response.json())
    payload = jwt.decode(login_response.access_token, SECRET_KEY, algorithms=[ALGORYTHM])
    user_id: str = payload.get("user_id")
    assert uuid.UUID(user_id) == user.id
    assert login_response.token_type == "bearer"


@pytest.mark.parametrize("email, password, status_code", [
    ("wrongemail@example.com", "pass", 403),
    ("usertest123@example.com", "wrong_password", 403),
    ("wrongemail@example.com", "wrong_password", 403),
])
def test_incorrect_login(client, email, password, status_code):
    response = client.post(
        "/login", data={"username": email, "password": password}
    )
    assert response.status_code == status_code
    assert response.json().get("detail") == "Invalid Credentials"
