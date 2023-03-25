from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    demo_qa_element = ElementsPage(browser)
    demo_qa_element.visit()
    # demo_qa_element.btn_sidebar_first.click()
    time.sleep(3)
    # assert demo_qa_element.btn_sidebar_first_textbox.exist()
    assert demo_qa_element.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    demo_qa_element = ElementsPage(browser)
    demo_qa_element.visit()
    assert demo_qa_element.btn_sidebar_first_checkbox.visible()
    demo_qa_element.btn_sidebar_first.click()
    time.sleep(3)
    assert not demo_qa_element.btn_sidebar_first_checkbox.visible()
