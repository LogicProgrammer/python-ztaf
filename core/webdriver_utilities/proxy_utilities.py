from . import config_keys as keys
from selenium.webdriver.common.proxy import Proxy, ProxyType


def get_proxy(config):
    proxy = Proxy()
    if config[keys.OPTIONS_PROXY_TYPE] == "MANUAL":
        proxy.proxy_type = ProxyType.MANUAL
        if config.__contains__(keys.OPTIONS_FTP_PROXY):
            proxy.ftp_proxy = config[keys.OPTIONS_FTP_PROXY]
        if config.__contains__(keys.OPTIONS_HTTP_PROXY):
            proxy.http_proxy = config[keys.OPTIONS_HTTP_PROXY]
        if config.__contains__(keys.OPTIONS_SSL_PROXY):
            proxy.http_proxy = config[keys.OPTIONS_SSL_PROXY]
    if config[keys.OPTIONS_PROXY_TYPE] == "AUTODETECT":
        proxy.proxy_type = ProxyType.AUTODETECT
        proxy.autodetect = True
    if config[keys.OPTIONS_PROXY_TYPE] == "PAC":
        proxy.proxy_type = ProxyType.PAC
        proxy.proxy_autoconfig_url = config[keys.OPTIONS_PROXY_PAC]
    if config[keys.OPTIONS_PROXY_TYPE] == "DIRECT":
        proxy.proxy_type = ProxyType.DIRECT
    return proxy
