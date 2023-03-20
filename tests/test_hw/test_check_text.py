from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_info(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_element_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert demo_qa_element_page.info_text_element.get_text() == 'Please select an item from left to start practice.'
