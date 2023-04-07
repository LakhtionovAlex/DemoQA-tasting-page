from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
import pytest


@pytest.mark.parametrize('pages', [Accordian, Alerts, DemoQa, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    assert page.metaView.get_dom_attribute('content') == 'width=device-width,initial-scale=1'
