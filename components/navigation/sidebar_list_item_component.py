from typing import Pattern

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str): #identifier внизу указываем только конечную часть локатора
        super().__init__(page)

        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon') #1
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text') #1
        self.button = page.get_by_test_id(f'{identifier}-drawer-list-item-button') #1

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.button).to_be_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)