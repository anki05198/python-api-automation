import pytest


@pytest.mark.ui
def test_product_sort_dropdown(page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Verify products page
    assert "inventory" in page.url

    # Select price: low to high
    dropdown = page.locator(".product_sort_container")
    dropdown.select_option(label="Price (low to high)")

    # Verify selected option
    assert dropdown.input_value() == "lohi"