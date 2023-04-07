from pages.slider import Slider
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest
import allure


@allure.title('test_slider')
@pytest.mark.smoke
def test_slider(browser):
    slider_page = Slider(browser)
    slider_page.visit()
    action_chains = ActionChains(browser)

    assert slider_page.slider.visible()
    assert slider_page.slider_input.visible()
    assert slider_page.slider_range.get_dom_attribute('value') == '25'
    action_chains.click_and_hold(slider_page.slider_range.find_element()).move_by_offset(2, 0).release().perform()
    assert slider_page.slider_range.get_dom_attribute('value') == '50'
    time.sleep(4)
