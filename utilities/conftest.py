import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

_URL = "https://www.saucedemo.com/"
_IMPLICIT_WAIT_TIME = 3


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(_URL)
    driver.maximize_window()
    driver.implicitly_wait(_IMPLICIT_WAIT_TIME)
    request.cls.driver = driver
    driver.implicitly_wait(2)

    yield

    driver.close()
