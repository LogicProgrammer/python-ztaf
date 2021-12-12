from urllib import request
from urllib.error import HTTPError


def get_http_response_status(url):
    try:
        conn = request.urlopen(url)
        return conn.getcode()
    except HTTPError as e:
        return e.code

