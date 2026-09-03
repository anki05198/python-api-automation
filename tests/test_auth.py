def test_get_current_user(dummyjson_client, auth_headers):

    response = dummyjson_client.get(
        "/auth/me",
        headers=auth_headers
    )

    assert response.status_code == 200

    data = response.json()

    assert "username" in data
    assert data["username"] == "emilys"


def test_get_current_user_without_token(dummyjson_client):
    response = dummyjson_client.get("/auth/me")
    assert response.status_code == 401


def test_get_current_user_with_invalid_token(dummyjson_client):
    headers = {
        "Authorization" : "Bearer invalid-token"
    }
    response = dummyjson_client.get("/auth/me",
                                    headers = headers)

    assert response.status_code == 401