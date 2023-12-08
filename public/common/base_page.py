# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @author           Echo
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import os
from typing import *
import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import globalparam
from public.common.basepage_abc import BasePageABC
from selenium import webdriver
from public.common.exceptions import InvalidArgumentException, UnsupportedBrowserException, NameError, ValueError, \
    NoSuchElementException, TimeoutException, ElementNotInteractableException, AssertionError, ElementNotSelectableException

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
        """
        open url
        :param url: 打开网页
        :return:
        """
        try:
            self.driver.get(url)
            self.log.success(f"Navigated to {url}.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException(f"Unable to load {url}.")

    def max_window(self) -> None:
        """
        maximize window
        :return:
        """
        try:
            self.driver.maximize_window()
            self.log.success("Maximized the window.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to maximize the window.")

    def set_window(self, width: int, height: int) -> None:
        """
        set window size
        :param width: 宽
        :param height: 高
        :return:
        """
        try:
            self.driver.set_window_size(width, height)
            self.log.success(f"Set the window size to {width}x{height}.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to set the window size.")

    def refresh(self) -> None:
        """
        refresh browser
        :return:
        """
        try:
            self.driver.refresh()
            self.log.success("Refreshed the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to refresh the browser.")

    def close(self) -> None:
        """
        close browser
        :return:
        """
        try:
            self.driver.close()
            self.log.success("Closed the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to close the browser.")

    def quit(self) -> None:
        """
        quit browser
        :return:
        """
        try:
            self.driver.quit()
            self.log.success("Quit the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to quit the browser.")

    def wait_visible(self, locator: Text) -> None:
        """
        等待元素可见
        :param locator: 元素路径
        :return:
        """
        self.wait.until(EC.visibility_of_element_located(self.by_value(locator)))

    def get_element(self, locator: Text, whetherWait: bool = True) -> WebElement:
        """
        获取元素
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            if whetherWait:
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
        """
        获取一组元素
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            if whetherWait:
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
        """
        点击元素
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).click()
            self.log.success(f"Click element {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def input(self, locator, text: Text, whetherWait: bool = True) -> None:
        """
        输入文本
        :param locator: 元素路径
        :param text: 文本
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).send_keys(text)
            self.log.success(f"Input '{text}' to {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def clear(self, locator: Text, whetherWait: bool = True) -> None:
        """
        清空文本
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).clear()
            self.log.success(f"Clear the text content of {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def clear_and_input(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        """
        清空文本并输入
        :param locator: 元素路径
        :param text: 文本
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).clear()
            self.get_element(locator, whetherWait).send_keys(text)
            self.log.success(f"Clear and input '{text}' to {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def get_text(self, locator: Text, whetherWait: bool = True) -> Text:
        """
        获取文本
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            text = self.get_element(locator, whetherWait).text
            self.log.success(f"Get text: '{text}' from {locator}, Spend {time.time() - t1} seconds.")
            return text
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def get_url(self) -> Text:
        """
        获取当前url
        :return:
        """
        url = self.driver.current_url
        self.log.success(f"Get url: {url}.")
        return url

    def get_attribute(self, locator: Text, attribute: Text, whetherWait: bool = True) -> Text:
        """
        获取属性的值
        :param locator: 元素路径
        :param attribute: 属性
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            text = self.get_element(locator, whetherWait).get_attribute(attribute)
            self.log.success(f"Get attribute: {text} from {locator}, Spend {time.time() - t1} seconds.")
            return text
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def move_to_element(self, locator: Text, whetherWait: bool = True) -> None:
        """
        鼠标悬停
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            ActionChains(self.driver).move_to_element(self.get_element(locator, whetherWait)).perform()
            self.log.success(f"Move to element {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def switch_to_frame(self, locator: Text, whetherWait: bool = True) -> None:
        """
        切换frame
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.driver.switch_to.frame(self.get_element(locator, whetherWait))
            self.log.success(f"Switch to frame {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def switch_to_default_content(self) -> None:
        """
        切换到默认frame
        :return:
        """
        t1 = time.time()
        try:
            self.driver.switch_to.default_content()
            self.log.success(f"Switch to default content, Spend {time.time() - t1} seconds.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to switch to default content.")

    def click_hyperlink(self, locator: Text, whetherWait: bool = True) -> None:
        """
        点击超链接
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).click()
            self.log.success(f"Click hyperlink {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def switch_to_new_window(self) -> None:
        """
        切换到新窗口
        :return:
        """
        t1 = time.time()
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.log.success(f"Switch to new window, Spend {time.time() - t1} seconds.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to switch to new window.")

    def select(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        """
        下拉框选择
        :param locator: 元素路径
        :param text: 文本
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            Select(self.get_element(locator, whetherWait)).select_by_visible_text(text)
            self.log.success(f"-Select the drop-down box {text} from {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

    def get_selected(self, locator: Text, whetherWait: bool = True) -> Text:
        """
        获取选中的值
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            text = Select(self.get_element(locator, whetherWait)).first_selected_option.text
            self.log.success(f"Get selected value: {text} from {locator}, Spend {time.time() - t1} seconds.")
            return text
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def get_options(self, locator: Text, whetherWait: bool = True) -> List[Text]:
        """
        获取选项
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            text = [option.text for option in Select(self.get_element(locator, whetherWait)).options]
            self.log.success(f"Get options: {text} from {locator}, Spend {time.time() - t1} seconds.")
            return text
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")

    def assert_text(self, locator: Text, expected_text: Text, whetherWait: bool = True) -> None:
        """
        断言文本
        :param locator: 元素路径
        :param expected_text: 预期结果
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            actualResult = self.get_text(locator, whetherWait)
            assert actualResult == expected_text, self.log.error(f"Actual text '{actualResult}' does not match expected text '{expected_text}'")
            self.log.success(
                f"Successfully asserted text: {expected_text} from {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except AssertionError:
            raise AssertionError(f"Actual text '{actualResult}' does not match expected text '{expected_text}'")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception:
            self.take_screenshot()

    def assert_text_contains(self, locator: Text, expected_text: Text, whetherWait: bool = True) -> None:
        """
        模糊断言
        :param locator: 元素路径
        :param expected_text: 预期结果
        :param whetherWait: 是否等待
        """
        t1 = time.time()
        try:
            actual_text = self.get_text(locator, whetherWait)
            assert expected_text in actual_text, self.log.error(
                f"Actual text '{actual_text}' does not match expected text '{expected_text}'"
            )
            self.log.success(
                f"Successfully asserted that text: {expected_text} is in {locator}, Spend {time.time() - t1} seconds.")
        except AssertionError:
            raise AssertionError(f"Actual text '{actual_text}' does not match expected text '{expected_text}'")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception:
            self.take_screenshot()

    def submit(self, locator: Text, whetherWait: bool = True) -> None:
        """
        提交
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.get_element(locator, whetherWait).submit()
            self.log.success(f"Submit {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

    def execute_script(self, script: Text) -> None:
        """
        执行js代码
        :param script: javascript代码
        :return:
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.log.success(f"Execute script: {script}, Spend {time.time() - t1} seconds.")
        except Exception:
            raise Exception(f"Unable to execute javascript scripts: {script}, Spend {time.time() - t1} seconds.")

    def accept_alert(self) -> None:
        """
        接受alert
        :return:
        """
        t1 = time.time()
        try:
            self.driver.switch_to.alert.accept()
            self.log.success(f"Accept warning box, Spend {time.time() - t1} seconds.")
        except Exception:
            raise Exception(f"Unable to accept alert, Spend {time.time() - t1} seconds.")

    def take_screenshot(self) -> None:
        """
        截图
        :return:
        """
        t1 = time.time()
        try:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_name = os.path.join(globalparam.screenshot_path, f"screenshot_{timestamp}.png")
            self.driver.save_screenshot(screenshot_name)
            self.log.success(f"Get the current window screenshot,path: {screenshot_name}, Spend {time.time() - t1} seconds.")
        except Exception:
            raise Exception(f"Unable to take screenshot, Spend {time.time() - t1} seconds.")

    @staticmethod
    def by_value(locator: Text) -> Tuple[Text, Text]:
        """
        处理元素路径
        :param locator: 元素路径
        :return:
        """
        if "->" not in locator:
            raise ValueError(f"Invalid positioning syntax. Expected format: 'by->value', but actual format: {locator}.")

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
    b.assert_text(baidu_click_loc, "百度一下")
    time.sleep(3)
