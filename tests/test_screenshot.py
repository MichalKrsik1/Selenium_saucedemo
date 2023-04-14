from utilities.base_class import Base
from page_objects.login_page import LoginPage
from utilities.conftest import setup


class TestScreenshot(Base):

    def test_screenshot(self, setup):
        log = self.get_logger()
        login_page = LoginPage(self.driver)
        inventory_page = login_page.login()
        inventory_page.get_bike_light()

        self.take_screenshot()
        login_page = self.log_out()
        log.info(f"Title of the page is: {login_page.get_title()}")
        assert login_page.get_title() == "Swag Labs"
