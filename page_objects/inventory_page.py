from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    bike_light = (By.LINK_TEXT, "Sauce Labs Bike Light")
    sort_items = (By.XPATH, "//select[@class='product_sort_container']")
    products = (By.XPATH, "//div[@class='pricebar']/button")

    def get_bike_light(self):
        product_page_1 = self.driver.find_element(*InventoryPage.bike_light).click()
        return product_page_1

    # Price (low to high)
    def sort_by(self, text):
        sort_options = Select(self.driver.find_element(*InventoryPage.sort_items))
        sort_options.select_by_visible_text(text)

    def select_x_items(self, x):
        counter = 1
        product_list = self.driver.find_elements(*InventoryPage.products)
        for prod in product_list:
            if counter <= x:
                prod.click()
                counter += 1
            else:
                break
