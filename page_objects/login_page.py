import time
from selenium.webdriver.common.by import By
from page_objects.inventory_page import InventoryPage

USER_NAME = "standard_user"
PASSWORD = "secret_sauce"


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    title = (By.CLASS_NAME, "login_logo")

    def login(self):
        time.sleep(1)
        self.driver.find_element(*LoginPage.user_field).send_keys(USER_NAME)
        self.driver.find_element(*LoginPage.password_field).send_keys(PASSWORD)
        self.driver.find_element(*LoginPage.login_button).click()
        inventory_page = InventoryPage(self.driver)
        return inventory_page

    def get_title(self):
        return self.driver.find_element(*LoginPage.title).text
