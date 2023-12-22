import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Profile(BasePage):
    def open_profile_page(self):
        time.sleep(2)
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/panel/profile")

    def assert_name_and_last_name_are_right(self):
        time.sleep(2)
        elem = self.driver.find_element(By.XPATH, "//body//p")
        assert elem.text == "TesterName TesterSurname"


