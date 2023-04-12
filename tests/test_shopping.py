from utilities.base_class import Base
from page_objects.login_page import LoginPage
from utilities.conftest import setup
import time


class TestA(Base):
    test_data_cost = ("41.97", "3.36")
    test_data_message = "Thank you for your order!"

    def test_shopping(self, setup):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        log.info("Logging into page")
        inventory_page = login_page.login()

        log.info("Sort products and select them")
        inventory_page.sort_by("Price (low to high)")
        inventory_page.select_x_items(4)
        checkout_page = self.open_checkout()
        log.info("Remove product")
        time.sleep(3)
        checkout_page.remove_product()
        checkout_add_page = checkout_page.get_checkout()
        checkout_add_page.fill_details()
        checkout_overview = checkout_add_page.continue_shopping()
        checkout_overview.scroll_down()
        log.info(f"Price and tax: {checkout_overview.get_cost() == TestA.test_data_cost}")
        complete_page = checkout_overview.finish_shopping()
        log.info(f"Complete message: {complete_page.get_success_message() == TestA.test_data_message}")





        time.sleep(3)
