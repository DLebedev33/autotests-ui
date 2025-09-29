from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()
    # focus - ставит фокус на элемент (поле емайл), то есть мы сможем печатать в это поле с клавиатуры

    for char in 'user@gmail.com':
        page.keyboard.type(char, delay = 300)
        # В фокус мы печатаем это значение, то есть у нас наведётся на нужное поле и наберётся это значение
        # Если добавить к (char, delay = 300) он будет писать каждую букву с задержкой в 300 мс

    page.keyboard.press("ControlOrMeta+A")
    # Скопирует значение user@gmail.com, работает только с focus и обязательно её выводим из "for char" в новый абзац!!!

    page.wait_for_timeout(5000)