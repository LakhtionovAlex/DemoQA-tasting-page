from pages.form_page import FormPage
import time


def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.state.send_keys('NCR')
    form_page.state.enter()
    time.sleep(2)
    form_page.city.send_keys('Delhi')
    form_page.city.enter()
    time.sleep(5)

