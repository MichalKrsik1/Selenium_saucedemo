import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from page_objects.checkout_page import CheckoutPage
from page_objects.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class Base:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("log.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)
        return logger

    def take_screenshot(self):
        self.driver.save_screenshot("screenshot.png")

    def log_out(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        login_page = LoginPage(self.driver)

        return login_page

    def open_checkout(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        checkout_page = CheckoutPage(self.driver)

        return checkout_page

    def refresh(self):
        self.driver.refresh()
