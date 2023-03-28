from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    demo_qa_modal = ModalDialogs(browser)
    demo_qa_modal.visit()
    assert demo_qa_modal.btn_submenu.check_count_elements(5)


def test_navigation_modal(browser):
    demo_qa_modal = ModalDialogs(browser)
    demo_qa_page = DemoQa(browser)
    demo_qa_modal.visit()
    browser.refresh()
    demo_qa_modal.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == demo_qa_page.pageData['title']
    browser.set_window_size(1000, 1000)
