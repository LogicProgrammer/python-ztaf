import requests


class RestClient:

    def __init__(self):
        self.session = requests.Session()
        self.header = {}

    def add_auth(self, auth):
        self.session.auth = auth

    def add_header(self, header):
        self.header.update(header)

    def clear_header(self):
        self.header.clear()

