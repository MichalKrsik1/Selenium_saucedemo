from selenium.webdriver.common.by import By


class CompletePage:

    def __init__(self, driver):
        self.driver = driver

    finish_btn = (By.CLASS_NAME, "complete-header")

    def get_success_message(self):
        return self.driver.find_element(*CompletePage.finish_btn).text
