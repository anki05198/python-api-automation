# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)

# assert response.status_code == 200
#     f"Expected 200 but got {response.status_code}"

# data = response.json()

# assert "id" in data
# assert data["id"] == 1, \
#     f"Expected ID 1 but got {data['id']}"

# assert isinstance(data["id"], int)

# print("API test passed")
# print(type(data))
# print(len(data))
# print(data[0])
# print(data[0]["id"])

# print(data[0]["title"])
# print(data[1]["id"])
# print(data[1]["title"])
# for post in data:
#     print(f"ID: {post['id']} | Title: {post['title']}")

# for post in data:
#     assert "id" in post

# for post in data:
#     assert isinstance(post["id"], int)



# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)

# assert response.status_code == 200

# data = response.json()

# assert isinstance(data, list)
# assert len(data) == 100

# for post in data:
#     assert "id" in post
#     assert isinstance(post["id"], int)

# print("All API tests passed")



# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# updated_data = {
#     "id" : 1,
#     "title": "API Testing",
#     "body": "Learning Python API automation",
#     "userId": 1
# }

# response = requests.post(url, json=post_data)

# print(response.status_code)
# print(response.text)

# response = requests.post(url, json = post_data)
# assert response.status_code == 201
# data = response.json()

# assert "id" in data
# assert data["title"] == "API Testing"
# assert data["body"] == "Learning Python API automation"
# assert data["userId"] == 1

# print("POST API test passed")

# response = requests.put(url,json = updated_data)
# print(response.status_code)
# print(response.text)
# assert response.status_code == 200
# data = response.json()
# assert data["title"] == "API Testing"
# assert data["userId"] == 1
# assert data["body"] == "Learning Python API automation"
# print("PUT API test passed")



# import requests
# url = "https://jsonplaceholder.typicode.com/posts/1"

# patch_data = {
#     "title" : "Updated with PATCH"
# } 

# response = requests.patch(url,json = patch_data)
# print(response.st)
# print(response.text)
# assert response.status_code == 200
# data = response.json()
# assert data["title"] == "Updated with PATCH"

# print("PATCH API Test Passed")


# import requests
# url = "https://jsonplaceholder.typicode.com/posts/1"

# response = requests.delete(url)
# print(response.status_code)
# print(response.text)

# assert response.status_code == 200
# print("DELETE API test passed")

# import requests

# post_id = 5

# url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

# response = requests.get(url)

# assert response.status_code == 200

# data = response.json()

# assert data["id"] == post_id

# print("GET booking/post test passed")



# import requests
# url = "https://jsonplaceholder.typicode.com/posts"

# params = {
#     "userId" : 1
# }

# response = requests.get(url,params = params)
# assert response.status_code == 200
# data = response.json()
# print(data)

import requests
url = "https://jsonplaceholder.typicode.com/posts"

token = "abc123"
headers = {
    "Authorization" : f"Bearer {token}"
}

print(headers)