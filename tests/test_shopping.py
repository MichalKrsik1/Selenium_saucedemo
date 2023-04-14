from utilities.base_class import Base
from page_objects.login_page import LoginPage
from utilities.conftest import setup
import time
from test_data.test_data_and_constants import TEST_DATA_COST, TEST_DATA_MESSAGE

NUMBER_OF_ITEMS = 4


class TestShopping(Base):

    def test_shopping(self, setup):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        inventory_page = login_page.login()

        inventory_page.sort_by("Price (low to high)")
        inventory_page.select_x_items(NUMBER_OF_ITEMS)
        checkout_page = self.open_checkout()
        time.sleep(3)
        checkout_page.remove_product()
        checkout_add_page = checkout_page.open_checkout()
        checkout_add_page.fill_details()
        checkout_overview = checkout_add_page.continue_shopping()
        checkout_overview.scroll_down()
        log.info(f"Price and tax: {checkout_overview.get_cost() == TEST_DATA_COST}")
        complete_page = checkout_overview.finish_shopping()
        success_message = complete_page.get_success_message()
        log.info(f"Complete message: {success_message == TEST_DATA_MESSAGE}")
        assert success_message == TEST_DATA_MESSAGE
