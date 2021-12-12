import logging
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By

import setup
from core.element_utilities.element_info import ElementInfo
from core.enums.element_type import ElementType
from core.enums.locator_type import LocatorType
from .abstract_page import AbstractPage

log = logging.getLogger(__name__)


def escape_quotes(text):
    """for escaping special characters"""
    parts = text.split("'")
    return "concat('" + "', \"'\" , '".join(parts) + "', '')"


def get_section(ini_file, section_name):
    """ this function is used for fetching locators section in provided ini file"""
    config = ConfigParser()
    config.read(ini_file)
    if config.has_section(section_name):
        return config[section_name]
    else:
        raise Exception(f"unable to find section {section_name} in {ini_file}")


class ElementUtil(AbstractPage):

    def __init__(self, driver: webdriver, version, application):
        super().__init__(driver)
        self.driver = driver
        self.version = version
        self.application = application

    def get_element_by_label(self, label):
        return self.get_element_by_locator(self.get_locator_info(label))

    def get_element_by_locator(self, locator: By):
        log.info(locator)
        element = self.wait_for_presence(locator)
        self.highlight(element)
        return element

    def get_locator_info(self, info: ElementInfo):
        if info.template is not ElementType.invalid:
            info.loc = self.construct_locator(info.template, info.value, info.index)
            info.loc_type = LocatorType.xpath
            info.type = info.template
            return (info.loc_type.value, info.loc)
        else:
            return (info.loc_type.value, "(%s)[%s]" % (info.loc, info.index)) if info.loc_type is LocatorType.xpath else (info.loc_type.value, info.loc)
        #     if info.loc_type == LocatorType.xpath:                
        #         info.loc = "(%s)[%s]" % (info.loc, info.index)

        # info.by_loc = (info.loc_type.value, info.loc)
        # return info

    def construct_locator(self, element_type: ElementType, label: str, index: int):
        loc_dir = setup.get_parent() + "/config/locator_templates/"
        section = get_section(loc_dir + self.application + ".ini", self.version)
        locator_template = str(section[str(element_type.name)]).replace("{label}", escape_quotes(label))
        return "(%s)[%s]" % (locator_template, index)

    def get_element_info(self, value):
        for obj in self.__dir__():
            if isinstance(getattr(self, obj), ElementInfo):
                if getattr(self, obj).value == value:
                    return getattr(self, obj)
        raise RuntimeError(f"unable to find the element with value : {value}")

