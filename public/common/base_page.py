# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @author           Echo
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
from typing import *
import selenium.common.exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import globalparam
from public.common.basepage_abc import BasePageABC
from selenium import webdriver
from public.common.exceptions import InvalidArgumentException, UnsupportedBrowserException, NameError, ValueError, \
    NoSuchElementException, TimeoutException, ElementNotInteractableException, ElementNotSelectableException

import time


class BasePage(BasePageABC):

    def __init__(self):
        t1 = time.time()
        browser = globalparam.browser.lower()
        browser_drivers = {
            "firefox": webdriver.Firefox,
            "chrome": webdriver.Chrome,
            "edge": webdriver.Edge
        }
        if browser in browser_drivers:
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument('ignore-certificate-errors')
                service = Service(globalparam.driver_path)
                self.driver: webdriver = browser_drivers[browser](options=options, service=service)
            else:
                self.driver = browser_drivers[browser]()
            self.wait: WebDriverWait = WebDriverWait(self.driver, timeout=20, poll_frequency=0.8)
            self.log.success(f"Start a new browser: {browser}, Spend {time.time() - t1} seconds.")
        else:
            raise UnsupportedBrowserException(f"Browser {browser} is not supported.")

    def open_url(self, url: Text) -> None:
        try:
            self.driver.get(url)
            self.log.success(f"Navigated to {url}.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException(f"Unable to load {url}.")

    def close(self) -> None:
        try:
            self.driver.close()
            self.log.success("Closed the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to close the browser.")

    def quit(self) -> None:
        try:
            self.driver.quit()
            self.log.success("Quit the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to quit the browser.")

    def wait_visible(self, locator: Text) -> None:
        self.wait.until(EC.visibility_of_element_located(self.by_value(locator)))

    def get_element(self, locator: Text, whetherWait: bool = True) -> WebElement:
        try:
            if whetherWait:
                t1 = time.time()
                self.wait_visible(locator)
                element = self.driver.find_element(*self.by_value(locator))
                return element
            else:
                return self.driver.find_element(*self.by_value(locator))
        except selenium.common.exceptions.NoSuchElementException:
            raise NoSuchElementException(f"Element {locator} not found, Spend {time.time() - t1} seconds.")
        except selenium.common.exceptions.TimeoutException:
            raise TimeoutException(
                f"Wait for element {locator} to be visible timeout, Spend {time.time() - t1} seconds.")

    def get_elements(self, locator: Text, whetherWait: bool = True) -> List[WebElement]:
        try:
            if whetherWait:
                t1 = time.time()
                self.wait_visible(locator)
                element = self.driver.find_elements(*self.by_value(locator))
                return element
            else:
                return self.driver.find_elements(*self.by_value(locator))
        except selenium.common.exceptions.NoSuchElementException:
            raise NoSuchElementException(f"Element {locator} not found, Spend {time.time() - t1} seconds.")
        except selenium.common.exceptions.TimeoutException:
            raise TimeoutException(
                f"Wait for element {locator} to be visible timeout, Spend {time.time() - t1} seconds.")

    def click(self, locator: Text, whetherWait: bool = True) -> None:
        try:
            t1 = time.time()
            self.get_element(locator, whetherWait).click()
            self.log.success(f"Click element {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def input(self, locator, text: Text, whetherWait: bool = True) -> None:
        try:
            t1 = time.time()
            self.get_element(locator, whetherWait).send_keys(text)
            self.log.success(f"Input '{text}' to {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    @staticmethod
    def by_value(locator: Text) -> Tuple[Text, Text]:
        if "->" not in locator:
            raise ValueError("Invalid positioning syntax. Expected format: 'by->value'.")

        by = locator.split("->")[0].strip()
        value = locator.split("->")[1].strip()

        by_string = {
            "id": "id",
            "name": "name",
            "xpath": "xpath",
            "css": "css selector",
            "tag": "tag name",
            "class": "class name",
            "link": "link text",
            "plink": "partial link text"
        }

        # 注意大小写需与字典中的保持一致
        if by not in by_string:
            raise NameError(f"Locator type '{by}' not supported.")
        locator = (by_string[by], value)
        return locator


if __name__ == '__main__':
    b = BasePage()
    b.open_url("https://www.baidu.com")
    baidu_loc = "id->kw"
    baidu_click_loc = "id->su"
    b.input(baidu_loc, "selenium")
    b.click(baidu_click_loc)
    time.sleep(3)
