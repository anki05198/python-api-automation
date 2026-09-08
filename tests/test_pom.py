import json
import os
import pytest

from config import UI_BASE_URL
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


with open("test_data/ui_data.json") as file:
    test_data = json.load(file)


@pytest.mark.ui
def test_add_product_using_pom(page):

    page.goto(UI_BASE_URL)

    login_page = LoginPage(page)

    password = os.getenv("SAUCE_PASSWORD")

    login_page.login(
        test_data["username"],
        password
    )

    assert "inventory" in page.url

    inventory_page = InventoryPage(page)

    inventory_page.add_first_product_to_cart()
    inventory_page.open_cart()

    assert "cart" in page.url