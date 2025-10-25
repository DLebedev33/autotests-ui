import pytest
from playwright.sync_api import sync_playwright, Page, expect


@pytest.mark.regression
@pytest.mark.registration
@pytest.mark.parametrize('email, username, password', [
("user.name@gmail.com", "username", "password")
])
def test_successful_registration(registration_page: Page, email: str, username: str, password: str, dashboard_page:
Page):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form(email, username, password)
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()