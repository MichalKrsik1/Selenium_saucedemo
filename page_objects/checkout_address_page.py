from selenium.webdriver.common.by import By
from page_objects.checkout_overview_page import CheckoutOverviewPage


class CheckoutAddressPage:
    _first_name = (By.ID, "first-name")
    _last_name = (By.ID, "last-name")
    _postal_code = (By.ID, "postal-code")
    _continue_btn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def fill_details(self, first="M", last="K", zip_code="1"):
        self.driver.find_element(*CheckoutAddressPage._first_name).send_keys(first)
        self.driver.find_element(*CheckoutAddressPage._last_name).send_keys(last)
        self.driver.find_element(*CheckoutAddressPage._postal_code).send_keys(zip_code)

    def continue_shopping(self):
        self.driver.find_element(*CheckoutAddressPage._continue_btn).click()
        return CheckoutOverviewPage(self.driver)
