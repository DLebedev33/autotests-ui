import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
# yield даёт нам делать какие то действия до теста и какие то действия после теста,
# если поставить return, то браузер закроется до начала теста
    browser.close()
