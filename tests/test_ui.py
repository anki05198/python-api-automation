from playwright.sync_api import sync_playwright


def test_login_debug():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        page.wait_for_url("**/inventory.html")

        assert "inventory" in page.url

        page.screenshot(path="login_success.png")

        browser.close()