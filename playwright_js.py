from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )
    # wait_until='networkidle' - Playwright подождёт пока загрузится страница, а только потом будет переписывать ниже

    # Выполняем JS-код для замены текста заголовка
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)
    # evaluate - запускает скрипты, то есть можно с помощью него запустить JS код
    # getElementById копируем локатор от заголовка (в данном случае копируем локатор id)
    # В title.textContent приписываем текст на который хотим изменить

    page.wait_for_timeout(5000)