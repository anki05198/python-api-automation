import os
import pytest
from config import UI_BASE_URL


@pytest.mark.ui
def test_login(page):
    page.goto(UI_BASE_URL)

    page.get_by_placeholder("Username").fill("standard_user")

    password = os.getenv("SAUCE_PASSWORD")
    page.get_by_placeholder("Password").fill(password)

    page.get_by_role("button", name="Login").click()

    page.wait_for_url("**/inventory.html")

    assert "inventory" in page.url