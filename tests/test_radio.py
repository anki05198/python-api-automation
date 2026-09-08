from playwright.sync_api import sync_playwright


def test_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.lambdatest.com/selenium-playground/")

        page.get_by_text("Radio Buttons Demo").click()

        radio = page.locator('input[name= "optradio"][value="Male"]')

        radio.check()

        assert radio.is_checked()

        browser.close()