from selenium.webdriver.common.by import By


def test_check_getting_started_title(browser):
    browser.get("https://www.selenium.dev")
    element = browser.find_element(By.XPATH, '//main//h2')
    assert element.text == "Getting Started"
