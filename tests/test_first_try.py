
def test_open_selenium_home_page(browser):
    browser.get("https://www.selenium.dev")
    assert browser.title == 'Selenium'


def test_open_selenium_home_page_2(browser):
    browser.get("https://www.selenium.dev")
    assert browser.title == 'selenium'


