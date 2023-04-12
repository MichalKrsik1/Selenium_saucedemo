from selenium.webdriver.common.by import By
from page_objects.checkout_overview_page import CheckoutOverviewPage


class CheckoutAddressPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    def fill_details(self, first="M", last="K", zip_code="1"):
        self.driver.find_element(*CheckoutAddressPage.first_name).send_keys(first)
        self.driver.find_element(*CheckoutAddressPage.last_name).send_keys(last)
        self.driver.find_element(*CheckoutAddressPage.postal_code).send_keys(zip_code)

    def continue_shopping(self):
        self.driver.find_element(*CheckoutAddressPage.continue_btn).click()
        checkout_overview = CheckoutOverviewPage(self.driver)
        return checkout_overview
