from pages.alerts import Alerts
import time


def test_check_alert(browser):
    page_alert = Alerts(browser)
    page_alert.visit()

    page_alert.timer_alertBatton.click()
    time.sleep(4)
    assert not page_alert.alert()
    time.sleep(2)
    assert page_alert.alert()
    page_alert.alert().accept()
