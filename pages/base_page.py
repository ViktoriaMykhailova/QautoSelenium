from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_my_profile_button(self):
        self.driver.find_element(By.ID, "userNavDropdown").click()

    def click_profile_in_dropdown_list(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div"
                                           "/app-user-nav/div/nav/div[1]/a[1]").click()

    def click_garage_in_dropdown_item(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div"
                                           "/app-user-nav/div/nav/a[1]").click()

    def click_settings_in_dropdown_list(self):
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div"
                                           "/app-user-nav/div/nav/div[1]/a[2]").click()
