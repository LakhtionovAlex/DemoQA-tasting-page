from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA",
            "validate": "was-validated",
            "first_name": 'Aleksandr',
            "new_first_name": 'Ivan',
            "last_name": 'Lakhtionov',
            "user_email": 'LahtionovAleksandr@icloud.com',
            "age": '33',
            "salary": '90000',
            "department": 'QA'
        }

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.user_form = WebElement(driver, '#userForm')
        self.btn_submit = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.new_entry = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.edit_entry = WebElement(driver, '#edit-record-4')
        self.delete_new_entry = WebElement(driver, '#delete-record-4')
        self.select = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.title_delete = WebElement(driver, '[title="Delete"]')
        self.rows_found = WebElement(driver, 'div.rt-noData')
        self.number_page = WebElement(driver, 'input[type=number]')
