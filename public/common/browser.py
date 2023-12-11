"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
**    @fileName         browser.py
**    @author           Echo
**    @EditTime         2023/12/11
"""
from typing import *

from selenium.webdriver.chrome.service import Service

from config import globalparam
from selenium import webdriver

from public.common.exceptions import UnsupportedBrowserException


def select_browser(browser=globalparam.browser.lower()):
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    dr = None
    if browser == "firefox":
        dr = webdriver.Firefox()
    elif browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('ignore-certificate-errors')
        service = Service(globalparam.driver_path)
        dr = webdriver.Chrome(options=options, service=service)
    elif browser == "edge":
        dr = webdriver.Edge()
    else:
        raise UnsupportedBrowserException(f"Browser {browser} is not supported.")
    return dr

