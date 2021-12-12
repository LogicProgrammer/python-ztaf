import logging

from selenium.webdriver import Keys

from core.element_utilities.element_info import ElementInfo
from core.selenium_helpers.element_util import ElementUtil
from web.app.google.element.google_home_elements import IGoogleHome

log = logging.getLogger(__name__)


class GoogleHomePage(ElementUtil, IGoogleHome):

    def __init__(self, driver, version, application):
        super().__init__(driver, version, application)

    def search(self, keyword):
        self.send_keys(self.get_element_by_label(self.search_box), keyword)
        self.send_keys(self.get_element_by_label(self.search_box), Keys.TAB)
        self.click(self.get_element_by_label(self.get_element_info("search button")))

    def assert_title(self, keyword):
        assert keyword in self.driver.title

