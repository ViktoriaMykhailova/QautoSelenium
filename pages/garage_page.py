import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Garage(BasePage):

    def open_garage_page(self):
       time.sleep(2)
       self.driver.get("https://qauto.forstudy.space/panel/garage")


    def click_add_car_button(self):
        self.driver.find_element(By.XPATH, "//body//button[text()='Add car']").click()

    def set_mileage(self):
        elem = self.driver.find_element(By.NAME, "mileage")
        elem.send_keys("500")

    def click_add_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]").click()

    def click_add_fuel_expense_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]").click()

    def clear_mileage(self):
        time.sleep(2)
        elem = self.driver.find_element(By.ID, "addExpenseMileage")
        elem.clear()

    def set_new_mileage(self):
        time.sleep(2)
        elem = self.driver.find_element(By.ID, "addExpenseMileage")
        elem.send_keys("1000")

    def set_number_of_liters(self):
        elem = self.driver.find_element(By.NAME, "liters")
        elem.send_keys("50")

    def set_total_cost(self):
        elem = self.driver.find_element(By.NAME, "totalCost")
        elem.send_keys("100")

    def click_add_an_expense_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]").click()
