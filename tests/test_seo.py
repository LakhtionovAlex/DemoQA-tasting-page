from pages.demoqa import DemoQa
from pages.accordian import Accordian
import pytest
import time


def test_seo(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']


@pytest.mark.parametrize('pages', [DemoQa, Accordian])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']

