from pages.webtables import WebTables
import time
from selenium.webdriver.common.by import By


def test_sort(browser):
    column_sort = ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department', 'Action']

    web_tables_page = WebTables(browser)
    web_tables_page.visit()

    for column in column_sort:
        browser.find_element(By.XPATH, f"//*[.='{column}']").click()
        assert browser.find_element(By.XPATH, f"//*[.='{column}']")\
            .get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
        time.sleep(1)
    time.sleep(5)
    browser.quit()
