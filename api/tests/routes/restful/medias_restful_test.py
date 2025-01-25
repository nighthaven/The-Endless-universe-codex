from tests.fixtures.media_factory import MediaFactory


class TestMediasRestful:
    def test_get_media_restful(self, client):
        media = MediaFactory()
        media2 = MediaFactory()
        response = client.get("/endless/medias")
        assert response.status_code == 200
        assert response.json().get("count") == 2
        assert response.json().get("results") == [
            {"name": media.name.value},
            {"name": media2.name.value},
        ]
