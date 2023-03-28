from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.radio_btn_male = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.radio_btn_female = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(2)')
        self.radio_btn_other = WebElement(driver, '#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(3)')
        self.user_number = WebElement(driver, '#userNumber')
