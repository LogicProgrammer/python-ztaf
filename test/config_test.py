import logging
import time
import setup
from core.webdriver_utilities.webdriver_provider import WebDriverProvider
from web.app.google.page.google_home_page import GoogleHomePage

log = logging.getLogger(__name__)


class TestClass:

    def test_webdriver(self):
        config = setup.get_configuration()
        provider = WebDriverProvider(config)
        driver = provider.get_driver()
        driver.get("http://www.google.com")
        time.sleep(1)
        driver.close()

    def test_pom(self):
        config = setup.get_configuration()
        provider = WebDriverProvider(config)
        driver = provider.get_driver()
        driver.get("http://www.google.com")
        time.sleep(1)
        page = GoogleHomePage(driver,"1.0","google")
        page.search("selenium")
        time.sleep(3)
        driver.close()
