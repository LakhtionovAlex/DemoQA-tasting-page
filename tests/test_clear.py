from pages.text_box import TextBox
import time


def test_clear(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    text_box_page.user_name.send_keys('ajfskga')
    time.sleep(2)
    text_box_page.user_name.clear()
    time.sleep(4)
    assert text_box_page.user_name.get_text() == ''
