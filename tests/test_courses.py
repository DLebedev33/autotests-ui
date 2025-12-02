import pytest
from playwright.sync_api import Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # 1. Навигация скрыта в фикстуре/page object
    # 2. Селекторы скрыты в классах страниц
    # 3. Assert скрыты в методах

    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_courses_button()
    courses_list_page.check_visible_empty_view()