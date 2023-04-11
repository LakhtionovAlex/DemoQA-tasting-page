from pages.progress_bar import ProgressBar
import pytest
import allure
import time


@allure.title('stop progress bar 51%')
@pytest.mark.smoke
def test_progress_bar(browser):
    progress_bar_page = ProgressBar(browser)

    progress_bar_page.visit()
    time.sleep(2)
    assert progress_bar_page.btn_start.exist()
    assert progress_bar_page.progress_download.get_dom_attribute('aria-valuenow') == '0'
    progress_bar_page.btn_start.click()
    while True:
        if progress_bar_page.progress_download.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.btn_start.click()
            break
    assert progress_bar_page.progress_download.get_dom_attribute('aria-valuenow') == '51'
    time.sleep(3)
