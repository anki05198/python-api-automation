import pytest


@pytest.mark.ui
def test_checkbox(page):
    page.goto("https://www.lambdatest.com/selenium-playground/")

    page.get_by_text("Checkbox Demo").click()

    checkbox = page.locator('input[name="option1"]')

    checkbox.check()

    assert checkbox.is_checked()