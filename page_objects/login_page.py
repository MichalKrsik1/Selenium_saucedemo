import time
from selenium.webdriver.common.by import By
from page_objects.inventory_page import InventoryPage


class LoginPage:
    """test commit name change"""

    def __init__(self, driver):
        self.driver = driver

    user_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    title = (By.CLASS_NAME, "login_logo")

    def login(self):
        user_name = "standard_user"
        password = "secret_sauce"
        time.sleep(1)
        self.driver.find_element(*LoginPage.user_field).send_keys(user_name)
        self.driver.find_element(*LoginPage.password_field).send_keys(password)
        self.driver.find_element(*LoginPage.login_button).click()
        inventory_page = InventoryPage(self.driver)
        return inventory_page

    def get_title(self):
        return self.driver.find_element(*LoginPage.title).text

