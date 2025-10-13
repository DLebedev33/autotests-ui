from playwright.sync_api import expect


def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_header).to_have_text('Courses')

    there_is_no_results_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(there_is_no_results_block).to_have_text('There is no results')

    icom_block = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icom_block).to_be_visible()

    text_block = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_block).to_have_text('Results from the load test pipeline will be displayed here')