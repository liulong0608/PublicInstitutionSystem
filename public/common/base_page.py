# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @author           Echo
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
from typing import *

import selenium.common.exceptions

from config import globalparam
from public.common.basepage_abc import BasePageABC
from selenium import webdriver
from public.common.exceptions import InvalidArgumentException, UnsupportedBrowserException

import time


class BasePage(BasePageABC):

    def __init__(self):
        t1 = time.time()
        browser = "chcrome"
        drivers = {
            "firefox": webdriver.Firefox,
            "chrome": webdriver.Chrome,
            "edge": webdriver.Edge
        }
        if browser in drivers:
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument('ignore-certificate-errors')
                self.driver = drivers[browser](options=options)
            else:
                self.driver = drivers[browser]()
            self.log.success(f"Start a new browser: {browser}, Spend {time.time() - t1} seconds.")
        else:
            raise UnsupportedBrowserException(f"Browser {browser} is not supported.")

    def open_url(self, url: Text) -> None:
        try:
            self.driver.get(url)
            self.log.success(f"Navigated to {url}.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException(f"Unable to load {url}.")


if __name__ == '__main__':
    b = BasePage()
    b.open_url("https://www.baidu.com")
