import pytest
from utilities.base_class import Base
from page_objects.login_page import LoginPage
from utilities.conftest import setup
import time


class TestMultipleAddresses(Base):

    def test_addresses(self, get_data, setup):
        self.driver.implicitly_wait(2)
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        log.info("Logging into page")
        inventory_page = login_page.login()

        inventory_page.select_x_items(1)
        checkout_page = self.open_checkout()
        checkout_address = checkout_page.get_checkout()
        checkout_address.fill_details(get_data["first_name"], get_data["last_name"], get_data["zip_code"])
        time.sleep(1)

    @pytest.fixture(params=[{"first_name": "Michal", "last_name": "Krsik", "zip_code": "62100"},
                            {"first_name": "Petra", "last_name": "Heczkova", "zip_code": "62101"},
                            {"first_name": "Jan", "last_name": "Brazdil", "zip_code": "62102"}])
    def get_data(self, request):
        return request.param
