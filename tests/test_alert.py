from pages.alerts import Alerts
import time
import allure


@allure.title('проверка окна алерта')
def test_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


@allure.title('проверка текста алерта')
def test_alert_text(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()


@allure.title('Отмена алерта')
def test_confirm(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.result.get_text() == 'You selected Cancel'


@allure.title('Проверка промта')
def test_prompt(browser):
    name = 'Aleksandr'
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.btn_prompt.click()
    time.sleep(2)
    alert_page.alert().send_keys(name)
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == f'You entered {name}'
