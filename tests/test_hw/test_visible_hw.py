from pages.accordian import Accordian
import time


def test_visible_accordion(browser):
    demo_qa_page = Accordian(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_element.visible()
    demo_qa_page.btn_section.click()
    time.sleep(2)
    assert not demo_qa_page.text_element.visible()


def test_visible_accordian_default(browser):
    demo_qa_page = Accordian(browser)
    demo_qa_page.visit()
    assert not demo_qa_page.text_element_1.visible()
    assert not demo_qa_page.text_element_2.visible()
    assert not demo_qa_page.text_element_3.visible()
