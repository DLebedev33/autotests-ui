import pytest
from playwright.sync_api import Page


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: Page, create_course_page: Page):

    courses_list_page.click_create_courses_button()

    create_course_page.check_visible_create_course_title()

    create_course_page.check_visible_create_course_button()
    create_course_page.check_disabled_create_course_button()

    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()

    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.png")

    create_course_page.check_visible_image_upload_view()

    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_courses_button()
    courses_list_page.check_visible_course_card(
        index= 0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )