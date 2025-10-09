from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.regression
@pytest.mark.autorization
def test_wrong_email_or_password_autorization():
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        # метод launch запускает нам браузер, в данном случае chromium
        # headless - это режим в котором запускается браузер. False, чтобы видеть всё, что он делает.
        page = chromium.new_page()
        # у объекта page мы вызовем метод goto, который нам откроет нужную страницу
        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        # вызываем get_by_test_id, который встроен в playwright, где login-form-email-input это локатор на котором завязывались
        # а locator('input') это как мы искали кнопку внутри div с data-testid (//div[@data-testid="login-form-email-input"]//div//input)
        # далее заполняется всё по аналогии
        email_input.fill('user.name@gmail.com')
        # fill- заполняет данными поле

        password_input = page.get_by_test_id('login-form-password-input').locator(
            'input')
        password_input.fill('password')
        # заполняем данные поля этим значенеим
        login_button = page.get_by_test_id('login-page-login-button')
        # вызываем локатор кнопки "Login"
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id(
            'login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        # expect(ожидаем), что переменная (wrong_email_or_password_alert) будет to_be_visible(видемая)
        # expect - это ожидание чего-либо (то есть мы ожидаем, что ошибка будет видна на странице)
        # to_be_visible - это мы хотим увидеть что-либо (в данном случае появляющуюся ошибку)
        expect(wrong_email_or_password_alert).to_have_text('Wrong email or password')
        # expect(ожидаем), что он to_have_text (имелл какой-либо текс), в данном случае "Wrong email or password"