import logging

from web.app.google.page.google_home_page import GoogleHomePage

log = logging.getLogger(__name__)


class Google:

    home_page: GoogleHomePage = None

    def __init__(self, driver):
        self.driver = driver
        self.application = "google"
        self.version = "1.0"

    def get_page(self, name):
        pages = {
            'google home page': self.get_home_page
        }
        return pages[name]()

    def get_home_page(self):
        self.home_page = self.home_page if self.home_page is not None else GoogleHomePage(self.driver, self.version,
                                                                                          self.application)
        return self.home_page
