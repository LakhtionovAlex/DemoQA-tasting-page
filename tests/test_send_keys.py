from pages.form_page import FormPage
import time

def test_send_keys(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.first_name.send_keys('Aleksandr')
    form_page.last_name.send_keys('Lakhtionov')
    form_page.radio_btn_male.click()
    time.sleep(1)
    form_page.radio_btn_female.click()
    time.sleep(1)
    form_page.radio_btn_other.click()
    form_page.user_number.send_keys('+79310080308')
    time.sleep(5)
