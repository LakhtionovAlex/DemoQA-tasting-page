from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.submit.check_css_new('color', 'rgba(255, 255, 255, 1)')
    assert text_box.submit.check_css_new('backgroundColor', 'rgba(8, 123, 255, 1)')
    assert text_box.submit.check_css_new('borderColor', 'rgba(0, 123, 255)')
