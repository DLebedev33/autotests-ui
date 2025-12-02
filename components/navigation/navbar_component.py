from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class NavbarComponent(BaseComponent): # унаследуем класс из файлка base_component, где мы указывали url
    def __init__(self, page: Page): # инициализуруем конструктор класса как в base_component
        super().__init__(page)

        self.app_title = page.get_by_test_id('navigation-navbar-app-title-text')
        self.welcom_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    def check_visible(self, username: str): # 1
        expect(self.app_title).to_be_visible()
        expect(self.app_title).to_have_text('UI Course')

        expect(self.welcom_title).to_be_visible()
        expect(self.welcom_title).to_have_text(f'Welcome, {username}!') #1
# Будет формироваться имя, которое идёт после username (Подсвечено цифрой 1)