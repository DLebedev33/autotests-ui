import pytest
from playwright.sync_api import sync_playwright, expect, Page

from pages.login_page import LoginPage


@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
], ids=[
        "invalid email and password",
        "invalid email and empty password",
        "an empty email and an invalid password"
])
def test_wrong_email_or_password_autorization(login_page: Page, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.fill_login_form(email = email, password = password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()