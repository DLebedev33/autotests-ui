from playwright.sync_api import sync_playwright, Request, Response


def log_request(request: Request):
    print(f'Request: {request.url}')


def log_respons(response: Response):
    print(f'Response: {response.url},  {response.status}')
# Вызываем функции для логирования запросов и ответов

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request)
    # on выводит url запросов и ответов
    page.remove_listener('request', log_request)
    # remove_listener - уберёт запросы из консоли, чтобы они не отображались
    page.on('response', log_respons)

    page.wait_for_timeout(5000)