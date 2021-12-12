from configparser import ConfigParser


class Configuration:
    config = ConfigParser()
    file_path = "config.ini"

    def __init__(self, file_path):
        self.file_path = file_path
        self.config.read(file_path)

    def get_browser_config(self):
        return self.config['browser settings']

    def get_selenium_config(self):
        return self.config['selenium']

    def get_locators_config(self):
        return self.config['locators']

