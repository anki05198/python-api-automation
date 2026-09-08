from playwright.sync_api import sync_playwright


def test_product_sort_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        # Login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Verify products page
        assert "inventory" in page.url

        # Select price: low to high
        dropdown = page.locator(".product_sort_container")
        dropdown.select_option(label = "Price (low to high)")

        # Verify selected option
        assert dropdown.input_value() == "lohi"

        browser.close()