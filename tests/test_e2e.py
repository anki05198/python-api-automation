import pytest

from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_logged_in_user_can_add_product(logged_in_page):

    page = logged_in_page

    assert "inventory" in page.url

    inventory_page = InventoryPage(page)

    inventory_page.add_first_product_to_cart()

    inventory_page.open_cart()

    assert "cart" in page.url