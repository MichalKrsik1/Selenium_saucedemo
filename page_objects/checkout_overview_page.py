from selenium.webdriver.common.by import By
from page_objects.complete_page import CompletePage


class CheckoutOverviewPage:

    def __init__(self, driver):
        self.driver = driver

    finish_btn = (By.ID, "finish")
    cost = (By.CLASS_NAME, "summary_subtotal_label")
    tax = (By.CLASS_NAME, "summary_tax_label")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, 600)")

    def finish_shopping(self):
        self.driver.find_element(*CheckoutOverviewPage.finish_btn).click()
        complete_page = CompletePage(self.driver)
        return complete_page

    def get_cost(self):
        cost_value = self.driver.find_element(*CheckoutOverviewPage.cost).text[13:]
        tax_value = self.driver.find_element(*CheckoutOverviewPage.tax).text[6:]
        return cost_value, tax_value
