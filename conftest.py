# import pytest

# from api.api_client import APIClient

# @pytest.fixture
# def api_client():
#     return APIClient("https://jsonplaceholder.typicode.com")

# @pytest.fixture
# def auth_token():
#     return "dummy-token"

# @pytest.fixture
# def auth_headers(auth_token):
#     return {
#         "Authorization": f"Bearer {auth_token}",
#         "Accept": "application/json"
#     }

# import pytest
# from api.api_client import APIClient


# @pytest.fixture
# def api_client():
#     return APIClient("https://jsonplaceholder.typicode.com")


# @pytest.fixture
# def dummyjson_client():
#     return APIClient("https://dummyjson.com")

# @pytest.fixture
# def auth_token(dummyjson_client):
#     login_data = {
#         "username": "emilys",
#         "password": "emilyspass",
#         "expiresInMins": 30
#     }

#     response = dummyjson_client.post("/auth/login", login_data)

#     assert response.status_code == 200

#     data = response.json()

#     return data["accessToken"]

# @pytest.fixture
# def auth_headers(auth_token):
#     return {
#         "Authorization": f"Bearer {auth_token}",
#         "Accept": "application/json"
#     }



import pytest
from api.api_client import APIClient
from config import BASE_URL,DUMMYJSON_URL

@pytest.fixture
def api_client():
    return APIClient(BASE_URL)

@pytest.fixture
def dummyjson_client():
    return APIClient(DUMMYJSON_URL)

@pytest.fixture
def auth_token(dummyjson_client):
    login_data = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    response = dummyjson_client.post("/auth/login", login_data)

    assert response.status_code == 200

    data = response.json()

    return data["accessToken"]


@pytest.fixture
def auth_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}",
        "Accept": "application/json"
    }