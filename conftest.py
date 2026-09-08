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


import os
import json
import pytest
from api.api_client import APIClient
from playwright.sync_api import sync_playwright
from config import BASE_URL, DUMMYJSON_URL, UI_BASE_URL, HEADLESS

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, or webkit"
    )

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

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to run tests on: chromium, firefox, or webkit"
    )

@pytest.fixture(params=["chromium", "firefox", "webkit"])
def browser_name(request):
    return request.param

@pytest.fixture
def page(browser_name):
    with sync_playwright() as p:

        if browser_name == "chromium":
            browser = p.chromium.launch(headless=HEADLESS)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=HEADLESS)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=HEADLESS)
        else:
            raise ValueError(
                f"Unsupported browser: {browser_name}"
            )

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            browser = item.callspec.params.get("browser_name", "unknown")
            screenshot_path = (
                f"reports/screenshots/{item.name}_{browser}.png"
            )

            page.screenshot(path=screenshot_path)

@pytest.fixture
def posts_data():
    with open("test_data/posts_data.json") as file:
        return json.load(file)


@pytest.fixture
def logged_in_page(page):
    page.goto(UI_BASE_URL)

    username = "standard_user"
    password = os.getenv("SAUCE_PASSWORD")

    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/inventory.html")

    return page