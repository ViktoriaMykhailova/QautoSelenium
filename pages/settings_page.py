import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Settings(BasePage):

    def open_settings_page(self):
        time.sleep(2)
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/panel/settings")

    def click_remove_my_account_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body//button[text()='Remove my account']").click()

    def click_remove_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body//button[text()='Remove']").click()
