from playwright.sync_api import sync_playwright


def test_checkbox():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground/")

        page.get_by_text("Checkbox Demo").click()

        checkbox = page.locator('input[name="option1"]')

        checkbox.check()

        assert checkbox.is_checked()

        browser.close()