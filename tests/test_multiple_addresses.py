import pytest
from utilities.base_class import Base
from page_objects.login_page import LoginPage
from utilities.conftest import setup
import time


class TestMultipleAddresses(Base):

    def test_addresses(self, get_data, setup):
        login_page = LoginPage(self.driver)
        inventory_page = login_page.login()

        inventory_page.select_x_items(1)
        checkout_page = self.open_checkout()
        checkout_address = checkout_page.open_checkout()
        checkout_address.fill_details(get_data["first_name"], get_data["last_name"], get_data["zip_code"])
        time.sleep(1)

    @pytest.fixture(params=[
        {"first_name": "John", "last_name": "Doe", "zip_code": "62110"},
        {"first_name": "Lady", "last_name": "Doe", "zip_code": "62111"},
        {"first_name": "Big", "last_name": "Boy", "zip_code": "62112"}
    ])
    def get_data(self, request):
        return request.param
