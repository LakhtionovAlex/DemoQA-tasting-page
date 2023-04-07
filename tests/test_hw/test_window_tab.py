import allure
import pytest
from pages.links import Links
import time


@allure.title('check href')
@pytest.mark.smoke
def test_window_tab(browser):
    link_page = Links(browser)
    link_page.visit()

    assert link_page.link_home.exist()
    assert link_page.link_home.get_text() == 'Home'
    assert link_page.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert len(browser.window_handles) == 1
    link_page.link_home.click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://demoqa.com/'
    assert len(browser.window_handles) == 2
    time.sleep(1)
