from selenium import webdriver
from selenium.webdriver.firefox import service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as firefox_service
from selenium.webdriver.chrome.service import Service as chrome_service

from . import config_keys as keys
from .proxy_utilities import get_proxy


def get_chrome_driver(config):
    """creating chrome driver using configuration provided in chrome.ini"""
    options = webdriver.ChromeOptions()
    # adding chrome options
    if config.__contains__(keys.CHROME_COMMAND_LINE_ARGS):
        if config[keys.CHROME_COMMAND_LINE_ARGS] != "":
            arguments = config[keys.CHROME_COMMAND_LINE_ARGS].split(";")
            for arg in arguments:
                options.add_argument(arg)
    if config.__contains__(keys.CHROME_OPTIONS_HEADLESS):
        if config[keys.CHROME_OPTIONS_HEADLESS] == 'true':
            options.add_argument('--headless')
        else:
            options.arguments.remove("--headless")
    if config.__contains__(keys.CHROME_OPTIONS_BINARY):
        if config[keys.CHROME_OPTIONS_BINARY] != "":
            options._binary_location = config[keys.CHROME_OPTIONS_BINARY]
    if config.__contains__(keys.OPTIONS_PROXY_TYPE):
        proxy = get_proxy(config)
        options.proxy = proxy
    if config.__contains__(keys.CHROME_OPTIONS_SET_ACCEPT_INSECURE_CERTS):
        if config[keys.CHROME_OPTIONS_SET_ACCEPT_INSECURE_CERTS] == "true":
            options.accept_insecure_certs = True
    if config.__contains__(keys.CHROME_OPTIONS_UNHANDLED_PROMPT_BEHAVIOUR):
        if config[keys.CHROME_OPTIONS_UNHANDLED_PROMPT_BEHAVIOUR] != "":
            options.unhandled_prompt_behavior = config[keys.CHROME_OPTIONS_UNHANDLED_PROMPT_BEHAVIOUR]
    # creating chrome driver
    driver_details = config[keys.CHROME_DRIVER]
    if driver_details == "latest":
        driver_path = ChromeDriverManager().install()
    elif driver_details.startsWith('@'):
        driver_details = driver_details.replace("@", "")
        driver_path = ChromeDriverManager(driver_details).install()
    elif driver_details.endswith(".exe"):
        driver_path = driver_details.strip()
    else:
        driver_path = ChromeDriverManager().install()
    cs = chrome_service(executable_path=driver_path)
    return webdriver.Chrome(options=options, service=cs)


def get_firefox_driver(config):
    options = webdriver.FirefoxOptions()
    # creating firefox driver
    driver_details = config[keys.FIREFOX_DRIVER]
    if driver_details == "latest":
        driver_path = GeckoDriverManager().install()
    elif driver_details.startsWith('@'):
        driver_details = driver_details.replace("@", "")
        driver_path = GeckoDriverManager(driver_details).install()
    elif driver_details.endswith(".exe"):
        driver_path = driver_details.strip()
    else:
        driver_path = GeckoDriverManager().install()
    fs = firefox_service(executable_path=driver_path)
    return webdriver.Firefox(options=options, service=fs)


def get_edge_driver(config):
    options = webdriver.EdgeOptions()
    # creating chrome driver
    driver_details = config[keys.FIREFOX_DRIVER]
    if driver_details == "latest":
        driver_path = EdgeChromiumDriverManager().install()
    elif driver_details.startsWith('@'):
        driver_details = driver_details.replace("@", "")
        driver_path = EdgeChromiumDriverManager(driver_details).install()
    elif driver_details.endswith(".exe"):
        driver_path = driver_details.strip()
    else:
        driver_path = EdgeChromiumDriverManager().install()
    return webdriver.Edge(options=options, executable_path=driver_path)
