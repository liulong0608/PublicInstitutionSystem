"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
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
        pass

    @abstractmethod
    def max_window(self) -> None:
        pass

    @abstractmethod
    def set_window(self, width: int, height: int) -> None:
        pass

    @abstractmethod
    def refresh(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def quit(self) -> None:
        pass

    @abstractmethod
    def wait_visible(self, locator: Text) -> None:
        pass

    @abstractmethod
    def get_element(self, locator: Tuple[Text, Text], whetherWait: bool = True) -> WebElement:
        pass

    @abstractmethod
    def get_elements(self, locator: Text, whetherWait: bool = True) -> List[WebElement]:
        pass

    @abstractmethod
    def click(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def input(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def clear(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def clear_and_input(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def get_text(self, locator: Text, whetherWait: bool = True) -> Text:
        pass

    @abstractmethod
    def get_url(self) -> Text:
        pass

    @abstractmethod
    def get_attribute(self, locator: Text, attribute: Text, whetherWait: bool = True) -> Text:
        pass

    @abstractmethod
    def move_to_element(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def switch_to_frame(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def switch_to_default_content(self) -> None:
        pass

    @abstractmethod
    def click_hyperlink(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def switch_to_new_window(self) -> None:
        pass

    @abstractmethod
    def select(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def get_selected(self, locator: Text, whetherWait: bool = True) -> Text:
        pass

    # 获取下拉框中所有的选项
    @abstractmethod
    def get_options(self, locator: Text, whetherWait: bool = True) -> List[Text]:
        pass

    @abstractmethod
    def assert_text(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def assert_text_contains(self, locator: Text, expected_text: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def submit(self, locator: Text, whetherWait: bool = True) -> None:
        pass

    @abstractmethod
    def executeScript(self, script: Text) -> None:
        pass

    @abstractmethod
    def accept_alert(self) -> None:
        pass

    @abstractmethod
    def take_screenshot(self) -> None:
        pass

    @abstractmethod
    def tab(self, locator: Text, whetherWait: bool = True) -> None:
        pass
