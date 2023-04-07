from pages.webtables import WebTables
import time
import allure
import pytest


@allure.title('Page fill check')
@allure.feature('Checking test statuses')
@allure.story('Checking for Adding and Removing Records')
@pytest.mark.xfail(condition=False, reason='Skipped test')
def test_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()
    assert web_tables_page.btn_add

    web_tables_page.btn_add.click()
    assert web_tables_page.user_form.visible()

    web_tables_page.btn_submit.click()
    assert web_tables_page.user_form.get_dom_attribute('class') == web_tables_page.pageData['validate']

    web_tables_page.first_name.send_keys(web_tables_page.pageData["first_name"])
    web_tables_page.last_name.send_keys(web_tables_page.pageData["last_name"])
    web_tables_page.user_email.send_keys(web_tables_page.pageData["user_email"])
    web_tables_page.age.send_keys(web_tables_page.pageData["age"])
    web_tables_page.salary.send_keys(web_tables_page.pageData["salary"])
    web_tables_page.department.send_keys(web_tables_page.pageData["department"])
    time.sleep(1)
    web_tables_page.btn_submit.click()
    time.sleep(1)
    assert web_tables_page.new_entry.get_text() == web_tables_page.pageData["first_name"]
    web_tables_page.edit_entry.click()
    time.sleep(1)
    assert web_tables_page.user_form.visible()
    assert web_tables_page.first_name.get_dom_attribute('value') == web_tables_page.pageData["first_name"]
    web_tables_page.first_name.clear()
    time.sleep(1)
    web_tables_page.first_name.send_keys(web_tables_page.pageData["new_first_name"])
    web_tables_page.btn_submit.click()
    assert web_tables_page.new_entry.get_text() == web_tables_page.pageData["new_first_name"]
    time.sleep(1)
    web_tables_page.delete_new_entry.click()
    assert web_tables_page.new_entry.get_text() == ' '


@allure.title('Moving through the pages of the table')
@allure.feature('Checking test statuses')
@pytest.mark.smoke
def test_page_web_tables(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    web_tables_page.select.select('5')
    time.sleep(3)
    assert web_tables_page.btn_previous.get_dom_attribute('disabled')
    assert web_tables_page.btn_next.get_dom_attribute('disabled')

    while web_tables_page.btn_next.get_dom_attribute('disabled'):
        web_tables_page.btn_add.click()
        web_tables_page.first_name.send_keys(web_tables_page.pageData["first_name"])
        web_tables_page.last_name.send_keys(web_tables_page.pageData["last_name"])
        web_tables_page.user_email.send_keys(web_tables_page.pageData["user_email"])
        web_tables_page.age.send_keys(web_tables_page.pageData["age"])
        web_tables_page.salary.send_keys(web_tables_page.pageData["salary"])
        web_tables_page.department.send_keys(web_tables_page.pageData["department"])
        time.sleep(1)
        web_tables_page.btn_submit.click()

    time.sleep(2)
    assert not web_tables_page.btn_next.get_dom_attribute('disabled')
    web_tables_page.btn_next.click()
    assert web_tables_page.number_page.get_dom_attribute('value') == '2'
    time.sleep(2)
    web_tables_page.btn_previous.click()
    assert web_tables_page.number_page.get_dom_attribute('value') == '1'
    time.sleep(2)


@allure.title('удаление из таблицы')
def test_web_table(browser):
    web_tables_page = WebTables(browser)
    web_tables_page.visit()
    assert not web_tables_page.rows_found.exist()
    while web_tables_page.title_delete.exist():
        web_tables_page.title_delete.click()
    time.sleep(3)
    assert web_tables_page.rows_found.exist()
