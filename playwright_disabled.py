from playwright.sync_api import sync_playwright, expect

from playwright_authorization import login_button

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # headless=False - значит будем видеть браузер визуально
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_disabled()
    # Мы находим находим задизейбленную кнопку по локатору и expect(ожидаем), что она to be(быть) задизейблена
    # not_to_be_disabled - проверка, что кнопка не задизейблена

    page.wait_for_timeout(5000)