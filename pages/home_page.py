import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    def click_sign_up_button(self):
        self.driver.find_element(By.XPATH, "//body//button[text()='Sign up']").click()

    def open(self):
        self.driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def set_name(self):
        elem = self.driver.find_element(By.NAME, "name")
        elem.send_keys("TesterName")

    def set_lastname(self):
        elem = self.driver.find_element(By.NAME, "lastName")
        elem.send_keys("TesterSurname")

    def set_email(self):
        elem = self.driver.find_element(By.NAME, "email")
        elem.send_keys("testerqa49@gmail.com")

    def set_password(self):
        elem = self.driver.find_element(By.NAME, "password")
        elem.send_keys("Qa123456789")

    def set_repeat_password(self):
        elem = self.driver.find_element(By.NAME, "repeatPassword")
        elem.send_keys("Qa123456789")

    def click_register_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body//button[text()='Register']").click()

