"""         ==Coding: UTF-8==
**    @Project :        UIAutomationTestTemplate
**    @fileName         basepage_abc.py
**    @author           Echo
**    @EditTime         2023/12/5
"""
from abc import abstractmethod, ABC
from typing import *

from selenium.webdriver.remote.webelement import WebElement

from public.common.log import Log

import time


class BasePageABC(ABC):
    log = Log(stream=True).logger

    @abstractmethod
    def open_url(self, url: Text) -> None:
        """
        open url
        :param url: 打开网页
        :return:
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        close browser
        :return:
        """
        pass

    @abstractmethod
    def quit(self) -> None:
        """
        quit browser
        :return:
        """
        pass

    @abstractmethod
    def wait_visible(self, locator: Text) -> None:
        """
        等待元素可见
        :param locator: 元素路径
        :return:
        """
        pass

    @abstractmethod
    def get_element(self, locator: Tuple[Text, Text], whetherWait: bool = True) -> WebElement:
        """
        获取元素
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        pass

    @abstractmethod
    def get_elements(self, locator: Tuple[Text, Text]) -> List[WebElement]:
        """
        获取一组元素
        :param locator: 元素路径
        :return:
        """
        pass

    def click(self, locator: Tuple[Text, Text], whetherWait: bool = True) -> None:
        """
        点击元素
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        self.get_element(locator).click()