from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    _bike_light = (By.LINK_TEXT, "Sauce Labs Bike Light")
    _sort_items = (By.XPATH, "//select[@class='product_sort_container']")
    _products = (By.XPATH, "//div[@class='pricebar']/button")

    def get_bike_light(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(InventoryPage._bike_light)
        )
        self.driver.find_element(*InventoryPage._bike_light).click()

    def sort_by(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(InventoryPage._sort_items)
        )
        sort_options = Select(self.driver.find_element(*InventoryPage._sort_items))
        sort_options.select_by_visible_text(text)

    def select_x_items(self, x):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(InventoryPage._products)
        )
        product_list = self.driver.find_elements(*InventoryPage._products)
        for index, prod in enumerate(product_list):
            if index < x:
                prod.click()
            else:
                break
