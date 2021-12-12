import logging
import time

import pytest

import setup
from core.webdriver_utilities.webdriver_provider import WebDriverProvider
from web.app.google.google import Google

log = logging.getLogger(__name__)
config = setup.get_configuration()
provider = WebDriverProvider(config)


@pytest.fixture()
def setup(request):
    driver = provider.get_driver()
    google = Google(driver)
    request.instance.driver = driver
    request.instance.google = google
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestClass:

    def test_first(self):
        self.driver.get("https://www.google.com")
        self.google.get_page("google home page").search('selenium')
        time.sleep(5)
        assert "selenium" in self.driver.title

    def test_second(self):
        keyword = "selenium"
        self.driver.get("https://www.google.com")
        self.google.get_page("google home page").search(keyword)
        self.google.get_home_page().assert_title(keyword)
