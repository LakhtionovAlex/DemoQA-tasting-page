from pages.droppable import DropPable
from selenium.webdriver import ActionChains
import time


def test_drag_and_drop(browser):
    page = DropPable(browser)
    page.visit()
    action_chains = ActionChains(browser)
    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_element()).perform()
    time.sleep(2)
    assert page.drop.check_css('backgroundColor', 'steelblue')
    action_chains.drag_and_drop_by_offset(page.drag.find_element(), 1000, 200).perform()
    assert page.drop.check_css('backgroundColor', 'steelblue')
    time.sleep(3)
