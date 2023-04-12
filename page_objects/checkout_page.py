from selenium.webdriver.common.by import By
from page_objects.inventory_page import InventoryPage
from page_objects.checkout_address_page import CheckoutAddressPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    continue_shopping = (By.ID, "continue-shopping")
    checkout = (By.ID, "checkout")
    remove_prod = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")

    def get_continue_shopping(self):
        self.driver.find_element(*CheckoutPage.continue_shopping).click()
        prod_page = InventoryPage(self.driver)
        return prod_page

    def get_checkout(self):
        self.driver.find_element(*CheckoutPage.checkout).click()
        checkout_address_page = CheckoutAddressPage(self.driver)
        return checkout_address_page

    def remove_product(self):
        self.driver.find_element(*CheckoutPage.remove_prod).click()

