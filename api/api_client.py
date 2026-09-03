# import requests


# class APIClient:

#     def __init__(self, base_url):
#         self.base_url = base_url

#     def get(self, endpoint, params = None, headers = None):
#         url = f"{self.base_url}{endpoint}"
#         return requests.get(url,
#                             params = params,
#                             headers = headers,
#                             timeout = 10)

#     def post(self, endpoint, data,params = None, headers = None):
#         url = f"{self.base_url}{endpoint}"
#         return requests.post(url,
#                               json=data,
#                               params = params,
#                               headers = headers,
#                               timeout = 10)

#     def put(self, endpoint, data,params = None, headers = None):
#         url = f"{self.base_url}{endpoint}"
#         return requests.put(url, 
#                             json=data,
#                             params = params,
#                             headers=headers,
#                             timeout=10)

#     def patch(self, endpoint, data,params = None, headers = None):
#         url = f"{self.base_url}{endpoint}"
#         return requests.patch(url, 
#                               json=data,
#                               params = params,
#                               headers = headers,
#                               timeout = 10)

#     def delete(self, endpoint, params = None, headers = None):
#         url = f"{self.base_url}{endpoint}"
#         return requests.delete(url,
#                                params = params,
#                                headers = headers,
#                                timeout=10)


import requests
from logger import get_logger


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.logger = get_logger()
        self.session.headers.update({
            "Accept": "application/json"
        })

    def _request(self, method, endpoint, data=None, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"

        self.logger.info(
        f"Sending {method} request to {url}"
    )

        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                params=params,
                headers=headers,
                timeout=10
            )
            self.logger.info(
        f"Received response: {response.status_code}"
    )

            return response

        except requests.exceptions.Timeout:
            print(f"Request timed out: {url}")
            raise

        except requests.exceptions.ConnectionError:
            print(f"Connection error: {url}")
            raise

    def get(self, endpoint, params=None, headers=None):
        return self._request(
            "GET",
            endpoint,
            params=params,
            headers=headers
        )

    def post(self, endpoint, data=None, params=None, headers=None):
        return self._request(
            "POST",
            endpoint,
            data=data,
            params=params,
            headers=headers
        )

    def put(self, endpoint, data=None, params=None, headers=None):
        return self._request(
            "PUT",
            endpoint,
            data=data,
            params=params,
            headers=headers
        )

    def patch(self, endpoint, data=None, params=None, headers=None):
        return self._request(
            "PATCH",
            endpoint,
            data=data,
            params=params,
            headers=headers
        )

    def delete(self, endpoint, params=None, headers=None):
        return self._request(
            "DELETE",
            endpoint,
            params=params,
            headers=headers
        )