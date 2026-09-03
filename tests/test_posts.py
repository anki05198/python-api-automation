# import requests

# def test_get_post():
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     response = requests.get(url)
#     assert response.status_code == 200

# def test_get_invalid_post():
#     url = "https://jsonplaceholder.typicode.com/posts/99999"
#     response = requests.get(url)
#     assert response.status_code == 404

# to run command:  python -m pytest .\test_posts.py -v


# import requests


# def test_get_post(base_url):
#     url = f"{base_url}/posts/1"
#     response = requests.get(url)
#     assert response.status_code == 200

# def test_get_invalid_post(base_url):
#     url = f"{base_url}/posts/99999"
#     response = requests.get(url)
#     assert response.status_code == 404



# import requests
# import pytest

# @pytest.mark.parametrize("post_id",[1,2,3,4,5])
# def test_get_post(post_id):
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     response = requests.get(url)
#     assert response.status_code == 200

#     data = response.json()
#     assert data["id"] == post_id

# import json
# import requests
# import pytest

# with open("test_data/posts_data.json") as file:
#     test_data = json.load(file)

# print(test_data["valid_post_ids"])

# @pytest.mark.parametrize("post_id",test_data["valid_post_ids"])

# def test_get_post(post_id):
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     response = requests.get(url)
#     assert response.status_code == 200
#     data = response.json()
#     assert data["id"] == post_id

# def test_get_post(api_client):

#     response = api_client.get("/posts/1")

#     assert response.status_code == 200



# def test_create_post(api_client):

#     post_data = {
#         "title": "Python API Automation",
#         "body": "Learning API framework",
#         "userId": 1
#     }

#     response = api_client.post("/posts", post_data)

#     assert response.status_code == 201

#     data = response.json()

#     assert data["title"] == "Python API Automation"
#     assert data["body"] == "Learning API framework"
#     assert data["userId"] == 1

# def test_get_post_by_user(api_client):
#     response = api_client.get("/posts",params = {"userId" : 1})

#     assert response.status_code == 200
#     data = response.json()

#     for post in data:
#         assert post["userId"] == 1

# def test_get_post_with_headers(api_client):

#     headers = {
#         "Accept" : "application/json"
#     }

#     response = api_client.get("/posts/1",
#                               headers = headers)

#     assert response.status_code == 200

import json
import pytest

with open("test_data/posts_data.json") as file:
    test_data = json.load(file)

def test_get_post_with_auth_headers(api_client, auth_headers):

    response = api_client.get(
        "/posts/1",
        headers=auth_headers
    )

    assert response.status_code == 200

def test_get_post_response_body(api_client):

    response = api_client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data

def test_get_post_response_headers(api_client):

    response = api_client.get("/posts/1")

    assert response.status_code == 200

    content_type = response.headers.get("Content-Type")

    assert content_type is not None


@pytest.mark.parametrize(
    "post_id",
    test_data["valid_post_ids"]
)
def test_valid_post_ids(api_client, post_id):

    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == post_id


@pytest.mark.parametrize(
    "post_id",
    test_data["invalid_post_ids"]
)
def test_invalid_post_ids(api_client, post_id):

    response = api_client.get(f"/posts/{post_id}")

    assert response.status_code == 404