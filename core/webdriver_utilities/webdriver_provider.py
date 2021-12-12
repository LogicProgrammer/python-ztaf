import logging
from configparser import ConfigParser
from core.config_parser import Configuration
from .driver_utilities import get_chrome_driver, get_firefox_driver, get_edge_driver
import setup

log = logging.getLogger(__name__)


class WebDriverProvider:
    """this class is used for initiating web driver object of a given browser"""
    browser_config = ConfigParser()
    browser_config_folder = "browser_config"

    def __init__(self, configuration: Configuration):
        self.configuration = configuration

    def get_driver(self):
        browser_section = self.configuration.get_browser_config()
        browser_name = browser_section['browser_name']
        browser_config_name = browser_section['browser_config']
        return self.create_driver(browser_name, browser_config_name)

    def create_driver(self, browser_name, browser_config_name):
        log.info(f"browser name : {browser_name}")
        log.info(f"browser config : {browser_config_name}")
        if browser_name == "chrome":
            return self.create_chrome_driver(browser_config_name)
        elif browser_name == "firefox":
            return self.create_firefox_driver(browser_config_name)
        elif browser_name == "edge":
            return self.create_edge_driver(browser_config_name)
        else:
            log.info(f'given browser name is not compatible, initiating chrome')
            return self.create_chrome_driver('default')

    def create_chrome_driver(self, browser_config_name):
        self.browser_config.read(setup.get_browser_config_dir() + "/chrome.ini")
        log.info(f'available configurations are : {self.browser_config.sections()}')
        return get_chrome_driver(self.browser_config[browser_config_name])

    def create_firefox_driver(self, browser_config_name):
        self.browser_config.read(setup.get_browser_config_dir() + "/firefox.ini")
        log.info(f'available configurations are : {self.browser_config.sections()}')
        return get_firefox_driver(self.browser_config[browser_config_name])

    def create_edge_driver(self, browser_config_name):
        self.browser_config.read(setup.get_browser_config_dir() + "/edge.ini")
        log.info(f'available configurations are : {self.browser_config.sections()}')
        return get_edge_driver(self.browser_config[browser_config_name])
