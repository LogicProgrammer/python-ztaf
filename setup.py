import os
from configparser import ConfigParser

from core.config_parser import Configuration


def get_parent():
    return os.path.dirname(os.path.abspath(__file__))


def get_browser_config_dir():
    return get_parent() + "/config/browser"


def get_configuration():
    return Configuration(get_parent() + "/config/config.ini")


config = ConfigParser()
config.read("config/locator_templates/policy_center.ini")
list_of_sections = config.sections()

for section in list_of_sections:
    section_tuple = config[section]
    list_of_keys = section_tuple.keys()
    count = 0
    for key in list_of_keys:
        print(key, "=", count)
        count += 1
