from pages.text_box import TextBox
import time


def test_text_box(browser):
    name = 'Aleksandr'
    address = 'kjhvgafv'
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.user_name.send_keys(name)
    text_box_page.current_address.send_keys(address)
    text_box_page.submit.click_force()
    time.sleep(5)
    assert text_box_page.received_name.get_text() == f'Name:{name}'
    assert text_box_page.received_address.get_text() == f'Current Address :{address}'
