from pages.form_page import FormPage
import time


def test_send_keys(browser):
    form_page = FormPage(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('Aleksa')
    form_page.last_name.send_keys('Lakhti')
    form_page.radio_btn_male.click()
    form_page.email.send_keys('hgsk@sfgn.fd')
    form_page.user_number.send_keys('1111111111')
    form_page.btn_submit.click_force()
    time.sleep(5)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()
    time.sleep(5)

