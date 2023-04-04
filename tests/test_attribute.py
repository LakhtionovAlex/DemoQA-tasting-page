import allure
from pages.text_box import TextBox


@allure.feature('check attr')
@allure.story('Проверка отсутствие атрибута')
@allure.severity(allure.severity_level.BLOCKER)
def test_placeholder(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    assert text_box_page.user_name.get_dom_attribute('placeholder') == 'Full Name'


def test_fail():
    assert 111 == 222
