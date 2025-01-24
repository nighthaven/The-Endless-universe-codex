class TestAllLinkRestful:
    def test_all_link_restful(self, client):
        response = client.get("/endless")
        assert response.status_code == 200
        assert response.json().get("medias") == "http://127.0.0.1:8000/endless/medias"
        assert (
            response.json().get("anomalies")
            == "http://127.0.0.1:8000/endless/anomalies"
        )
        assert response.json().get("wonders") == "http://127.0.0.1:8000/endless/wonders"
