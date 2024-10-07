from src.serializer.media_serializer import MediaFormCreation
from src.models.media_models import MediaName


class TestCreateMedia:
    def test_create_media(self, authenticated_client):
        media = {
            "name":MediaName.ENDLESS_SPACE_2.value,
            "description":"test description"
        }
        response = authenticated_client.post("/media/", json=media)
        assert response.status_code == 201

    def test_create_media_with_unauthorized_user(self, client):
        media = {
            "name": MediaName.ENDLESS_SPACE_2.value,
            "description": "test description"
        }
        response = client.post("/media/", json=media)
        assert response.status_code == 401

class TestGetMedia:
    def test_get_media(self, client):
        response = client.get("/media/")
        assert response.status_code == 200

