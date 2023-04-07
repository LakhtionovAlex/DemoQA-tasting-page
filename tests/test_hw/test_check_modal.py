from pages.modal_dialogs import ModalDialogs
import requests
import time
import pytest


@pytest.mark.xfail(condition=False, reason='Skipped test')
def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    modal_page.btn_small_modal.click()
    modal_page.close_small_modal.click()
    time.sleep(1)

    modal_page.btn_large_modal.click()
    modal_page.close_large_modal.click()
    time.sleep(1)

    try:
        response = requests.head(modal_page.get_url())
        if response.status_code == 200:
            assert True
    except requests.ConnectionError:
        assert False
