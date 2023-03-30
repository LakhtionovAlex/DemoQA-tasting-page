from pages.form_page import FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.state.click_force()
    time.sleep(5)
    form_page.state1.arrow_down()
    time.sleep(5)
