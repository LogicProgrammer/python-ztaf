import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

log = logging.getLogger(__name__)


class AbstractPage:
    timeout = 30

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def launch_url(self, url):
        self.driver.get(url)

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def open_new_window(self, url=""):
        self.driver.execute_script(f"window.open('{url}','_blank');")

    def get_title(self):
        return self.driver.title

    def get_window_handles(self):
        return self.driver.window_handles

    def click(self, element):
        self.wait_for_clickable(element)
        element.click()

    def click_using_js(self, element):
        self.driver.execute_script("argument[0].click()", element)

    def click_using_actions(self, element):
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def send_keys(self, element, text):
        self.wait_for_clickable(element)
        element.send_keys(text)

    def send_keys_using_actions(self, element, text):
        ActionChains(self.driver).move_to_element(element).send_keys(element).perform()

    def is_element_present(self, by, sec=1):
        count = 0
        while sec > count:
            list_of_element = self.driver.find_elements(by)
            if len(list_of_element) > 0:
                return True
            else:
                time.sleep(1)
                log.info(f"trying to find the element {by}")
            count += 1
        return False

    def select_option(self, element, visible_text=None, index=None, value=None):
        self.wait_for_clickable(element)
        select = Select(element)
        if visible_text is not None:
            select.select_by_visible_text(visible_text)
        elif index is not None:
            select.select_by_index(index)
        elif value is not None:
            select.select_by_value(value)
        else:
            raise ValueError("Please provide option (index/visible_text/value) to select from the dropdown")

    def wait_for_presence(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator))

    def highlight(self, element):
        try:
            self.driver.execute_script("arguments[0].style.border='3px solid green';", element)
        except Exception as e:
            log.error("unable to highlight element!! :", element, e)
