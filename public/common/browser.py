"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
**    @fileName         browser.py
**    @author           Echo
**    @EditTime         2023/12/11
"""
import sys
from typing import *

from selenium.webdriver.chrome.service import Service

from config import globalparam
from selenium import webdriver

from public.common.exceptions import UnsupportedBrowserException

system_driver = sys.platform

def select_browser(browser=globalparam.browser.lower()):
    dc = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}
    dr = None
    if system_driver.lower() == "win32":
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
    elif system_driver.lower() == "linux":
        if browser == "firefox":
            dr = webdriver.Firefox()
        elif browser == "chrome":
            print("判断系统为linux")
            options = webdriver.ChromeOptions()
            options.add_argument('no-sandbox')
            options.add_argument("headless")  # 配置无头浏览器
            options.add_argument('disable-dev-shm-usage')
            options.add_argument('disable-gpu')  # 需要加上这个属性来规避bug
            service = Service(globalparam.linux_driver_path)
            dr = webdriver.Chrome(options=options, service=service)
        elif browser == "edge":
            dr = webdriver.Edge()
        else:
            raise UnsupportedBrowserException(f"Browser {browser} is not supported.")
        return dr
    else:
        raise UnsupportedBrowserException(f"System {system_driver} is not supported.")

