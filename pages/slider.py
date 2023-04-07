from pages.base_page import BasePage
from components.components import WebElement


class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/slider'
        super().__init__(driver, self.base_url)

        self.pageData = {
            "title": "DEMOQA"
        }
        self.slider = WebElement(driver, '#sliderContainer')
        self.slider_input = WebElement(driver, '#sliderValue')
        self.slider_range = WebElement(driver, '#sliderContainer > div.col-9 > span > input')
