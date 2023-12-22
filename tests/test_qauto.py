from pages.base_page import BasePage
from pages.profile_page import Profile
from pages.settings_page import Settings
from pages.garage_page import Garage
from pages.home_page import HomePage


def test_user_sign_up(browser):

    home_page = HomePage(browser)
    garage_page = Garage(browser)
    base_page = BasePage(browser)
    profile_page = Profile(browser)
    settings_page = Settings(browser)

    home_page.open()
    home_page.click_sign_up_button()

    home_page.set_name()
    home_page.set_lastname()
    home_page.set_email()
    home_page.set_password()
    home_page.set_repeat_password()
    home_page.click_register_button()

    garage_page.open_garage_page()

    base_page.click_my_profile_button()
    base_page.click_profile_in_dropdown_list()
    profile_page.open_profile_page()
    profile_page.assert_name_and_last_name_are_right()
    base_page.click_my_profile_button()
    base_page.click_garage_in_dropdown_item()

    garage_page.open_garage_page()

    garage_page.click_add_car_button()
    garage_page.set_mileage()
    garage_page.click_add_button()
    garage_page.click_add_fuel_expense_button()
    garage_page.clear_mileage()
    garage_page.set_new_mileage()
    garage_page.set_number_of_liters()
    garage_page.set_total_cost()
    garage_page.click_add_an_expense_button()
    base_page.click_my_profile_button()
    base_page.click_settings_in_dropdown_list()

    settings_page.open_settings_page()

    settings_page.click_remove_my_account_button()
    settings_page.click_remove_button()
