from playwright.sync_api import sync_playwright
# Мы полностью копируем скрипт из папки templates с названием
# playwrught_registration2 и теперь выполним как тест

def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        # context = нужен для сохранения данных (в данном случае для авторизации)
        page = context.new_page()

        page.goto(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator(
            'input')
        email_input.fill('user.name@gmail.com')

        username_input = page.get_by_test_id(
            'registration-form-username-input').locator('input')
        email_input.fill('username')

        password_input = page.get_by_test_id(
            'registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id(
            'registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')
        # Сохранение состояния в файл json, в данном случае в браузер в формате json

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto(
            'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        # данный блок нужен для того, чтобы после регистрации попасть сразу на страницу
        # сайта, по средствам состояния, который мы сохранили в файл json и подставили его

        page.wait_for_timeout(5000)