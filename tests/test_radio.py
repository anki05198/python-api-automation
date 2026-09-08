import pytest


@pytest.mark.ui
def test_radio_button(page):
    page.goto("https://www.lambdatest.com/selenium-playground/")

    page.get_by_text("Radio Buttons Demo").click()

    radio = page.locator('input[name="optradio"][value="Male"]')

    radio.check()

    assert radio.is_checked()