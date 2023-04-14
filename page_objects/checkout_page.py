from selenium.webdriver.common.by import By
from page_objects.inventory_page import InventoryPage
from page_objects.checkout_address_page import CheckoutAddressPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    _continue_shopping = (By.ID, "continue-shopping")
    _checkout = (By.ID, "checkout")
    _remove_prod = (By.XPATH, "//button[@class='btn btn_secondary btn_small cart_button']")

    def get_continue_shopping(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CheckoutPage._continue_shopping)
        )
        self.driver.find_element(*CheckoutPage._continue_shopping).click()
        return InventoryPage(self.driver)

    def open_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CheckoutPage._checkout)
        )
        self.driver.find_element(*CheckoutPage._checkout).click()
        return CheckoutAddressPage(self.driver)

    def remove_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CheckoutPage._remove_prod)
        )
        self.driver.find_element(*CheckoutPage._remove_prod).click()
