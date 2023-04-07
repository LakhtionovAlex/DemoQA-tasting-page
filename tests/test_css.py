from pages.text_box import TextBox


def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.submit.check_css('color', '#fff')
    assert text_box.submit.check_css('backgroundColor', '#007bff')
    assert text_box.submit.check_css('borderColor', '#007bff')
