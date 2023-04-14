from selenium.webdriver.common.by import By
from page_objects.complete_page import CompletePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    _finish_btn = (By.ID, "finish")
    _cost = (By.CLASS_NAME, "summary_subtotal_label")
    _tax = (By.CLASS_NAME, "summary_tax_label")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 600)")

    def finish_shopping(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutOverviewPage._finish_btn)
        )
        self.driver.find_element(*CheckoutOverviewPage._finish_btn).click()
        return CompletePage(self.driver)

    def get_cost(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutOverviewPage._cost)
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(CheckoutOverviewPage._tax)
        )

        cost_value = self.driver.find_element(*CheckoutOverviewPage._cost).text[13:]
        tax_value = self.driver.find_element(*CheckoutOverviewPage._tax).text[6:]
        return cost_value, tax_value
