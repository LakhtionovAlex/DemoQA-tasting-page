from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    demo_qa_element = ElementsPage(browser)
    assert demo_qa_element.equal_url()
