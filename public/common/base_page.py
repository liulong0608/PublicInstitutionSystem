# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @author           Echo
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import ast
import os
import sys
import time
from typing import *

import selenium.common.exceptions
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from config import globalparam
from config.globalparam import datas_path
from public.common.basepage_abc import BasePageABC
from public.common.exceptions import InvalidArgumentException, NameError, ValueError, \
    NoSuchElementException, TimeoutException, ElementNotInteractableException, AssertionException, \
    ElementNotSelectableException, WebDriverException
from utils.files_upload import upload_file

system_driver = sys.platform


class BasePage(BasePageABC):

    def __init__(self, selenium_driver: webdriver):
        self.driver: Union[BasePage, webdriver] = selenium_driver

    def open_url(self, url: Text) -> None:
        """
        打开网页
        :param url: url地址
        :return:
        """
        try:
            self.driver.get(url)
            self.log.success(f"Navigated to {url}.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException(f"Unable to load {url}.")

    def max_window(self) -> None:
        """
        窗口最大化
        :return:
        """
        try:
            self.driver.maximize_window()
            self.log.success("Maximized the window.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to maximize the window.")

    def set_window(self, width: int, height: int) -> None:
        """
        设置窗口大小
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
        刷新页面
        :return:
        """
        try:
            self.driver.refresh()
            self.log.success("Refreshed the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to refresh the browser.")

    def close(self) -> None:
        """
        关闭页面
        :return:
        """
        try:
            self.driver.close()
            self.log.success("Closed the browser.")
        except selenium.common.exceptions.InvalidArgumentException:
            raise InvalidArgumentException("Unable to close the browser.")

    def quit(self) -> None:
        """
        退出浏览器
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
        wait: WebDriverWait = WebDriverWait(self.driver, timeout=30, poll_frequency=0.8)
        wait.until(EC.visibility_of_element_located(self.by_value(locator)))

    def element_exists(self, locator: Text) -> bool:
        """
        判断元素是否存在
        :param locator: 元素路径
        :return:
        """
        try:
            self.driver.find_element(*self.by_value(locator))
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return False

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
            self.take_screenshot()
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
            self.take_screenshot()
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
        except ElementClickInterceptedException:  # 元素不可交互
            self.take_screenshot()
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:  # 元素不可选择
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except ElementNotVisibleException:  # 元素不可见
            raise ElementNotVisibleException(f"Element {locator} is not visible.")

    def input(self, locator, text: Any, whetherWait: bool = True) -> None:
        """
        输入文本
        :param locator: 元素路径
        :param text: 文本
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            element = self.get_element(locator, whetherWait)
            element.clear()
            element.send_keys(text)
            self.log.success(f"Input '{text}' to {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception as e:
            raise e

    def tab(self, locator: Text, whetherWait: bool = True) -> None:
        """
        模拟键盘TAB键
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.driver.find_element(*self.by_value(locator)).send_keys(Keys.TAB)
            self.log.success(f"Input '{Keys.TAB}' to {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception as e:
            raise e

    def clear(self, locator: Text, whetherWait: bool = True) -> None:
        """
        清空文本
        :param locator: 元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            element = self.get_element(locator, whetherWait)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            self.log.success(f"Clear the text content of {locator}, Spend {time.time() - t1} seconds.")
        except ElementNotInteractableException:
            ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception as e:
            raise e

    def clear_and_input(self, locator: Text, text: Text, whetherWait: bool = True) -> None:
        """
        清空文本并输入
        :param locator: 元素路径
        :param text: 文本
        :param whetherWait: 是否等待
        :return:
        """
        try:
            self.clear(locator, whetherWait)
            self.input(locator, text)
            self.tab(locator)
        except ElementNotInteractableException:
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")
        except Exception as e:
            raise e

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

    def switch_to_new_window(self, timeout: int = 10) -> None:
        """
        切换到新窗口
        :return:
        """
        current_windows = self.driver.window_handles
        t1 = time.time()
        try:
            # 等待新窗口出现
            new_window = WebDriverWait(self.driver, timeout).until(
                lambda driver: [window for window in driver.window_handles if window not in current_windows]
            )
            # 切换到新窗口
            self.driver.switch_to.window(new_window[0])
            self.log.success(f"Switched to new window, spent {time.time() - t1} seconds.")
        except TimeoutException:
            raise TimeoutException("A new window did not appear within the allotted time.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

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
            raise ElementNotInteractableException(f"Element {locator} is not interactable.")
        except ElementNotSelectableException:
            raise ElementNotSelectableException(f"Element {locator} is not selectable.")

    def assert_text(self, expected_text: str, actual_result: str, whether_wait: bool = True) -> None:
        """
        断言文本相等。
        :param expected_text: 预期的文本。
        :param actual_result: 实际结果的文本。
        :param whether_wait: 是否等待断言之前的某些条件。
        """
        assert isinstance(actual_result, str), "actual_result 必须是一个字符串"
        assert isinstance(expected_text, str), "expected_text 必须是一个字符串"
        start_time = time.time()
        try:
            assert actual_result == expected_text, f"The actual text '{actual_result}' does not match the expected text '{expected_text}'."
        except ElementNotInteractableException:
            self.take_screenshot()
            raise
        except ElementNotSelectableException:
            self.take_screenshot()
            raise
        except AssertionError as e:
            self.log.error(e.args[0])
            self.take_screenshot()
            raise AssertionException(e.args[0])
        except Exception:  # 其他意外异常仍应记录和截图
            self.take_screenshot()
            raise
        finally:
            elapsed_time = time.time() - start_time
            self.log.success(
                f"The successful assertion text: '{expected_text}' is from '{actual_result}' and takes {elapsed_time:.2f} seconds.")

    def assert_text_contains(self, expected_text: str, actual_text: str, whetherWait: bool = True) -> None:
        """
        断言实际文本包含预期的子字符串。

        :param expected_text: 预期的子字符串，用于断言其是否在实际文本中。
        :param actual_text: 需要检查的实际文本。
        :param whetherWait: 是否在断言前等待
        """
        assert isinstance(actual_text, str), "实际文本必须是字符串"
        assert isinstance(expected_text, str), "预期文本必须是字符串"

        start_time = time.time()
        try:
            assert expected_text in actual_text, f"Expect '{expected_text}' to appear in '{actual_text}'."
        except AssertionError as e:
            self.log.error(f"Assertion failure: {e}")
            self.take_screenshot()
            raise
        finally:
            elapsed_time = time.time() - start_time
            self.log.success(
                f"Assertions are present in the actual text with: '{expected_text}'. Time taken {elapsed_time:.2f} seconds.")

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

    def executeScript(self, script: Text) -> None:
        """
        执行js代码
        :param script: javascript代码
        :return:
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.log.success(f"Execute script: {script}, Spend {time.time() - t1} seconds.")
        except Exception as e:
            raise e
            # raise Exception(f"Unable to execute javascript scripts: {script}, Spend {time.time() - t1} seconds.")

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
            self.log.success(
                f"Get the current window screenshot,path: {screenshot_name}, Spend {time.time() - t1} seconds.")
        except Exception:
            raise Exception(f"Unable to take screenshot, Spend {time.time() - t1} seconds.")

    def htmlSelect(self, select_locator: Text, option_locator: Text, whetherWait: bool = True) -> None:
        """
        特殊下拉框
        :param select_locator: 下拉框元素路径
        :param option_locator: 选项元素路径
        :param whetherWait: 是否等待
        :return:
        """
        t1 = time.time()
        try:
            self.click(select_locator, whetherWait)
            time.sleep(0.5)
            self.click(f"xpath->//nz-option-item[@title='{option_locator}']", whetherWait)
            self.log.success(
                f"Special select option: {option_locator} from {select_locator}, Spend {time.time() - t1} seconds.")
            time.sleep(0.5)
        except Exception:
            raise Exception(
                f"Unable to select option: {option_locator} from {select_locator}, Spend {time.time() - t1} seconds.")

    def JsSelect(self, selector, value) -> None:
        """
        利用Js通过input输入的方式实现选择下拉框
        """
        t1 = time.time()
        script = """
        function setInputValue(selector, value) {
            /**
             * 设置输入框，触发事件
             * @param {String} selector ： 输入框的元素路径值*
             * @param {String} value： 输入框的值
             */
            // 获取元素
            const element = document.querySelector(selector);
            if (!element) return; // 如果没有找到元素，直接返回

            // 设置值
            element.value = value;

            // 创建并触发事件
            const event = new InputEvent('input', {
                'bubbles': true,
                'cancelable': true,
            });
            element.dispatchEvent(event);
        }
        setInputValue("%s", "%s");
        """ % (selector, value)
        try:
            self.executeScript(script)
            self.log.success(
                f"Javascript execute code to select option: {value} from {selector}, Spend {time.time() - t1} seconds.")
        except WebDriverException:
            raise WebDriverException(f"Unable to execute javascript to select option: {value} from {selector}.")

        except Exception as e:
            raise e

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

    def click_manager(self) -> None:
        _manager_menu_loc = 'xpath->//div[contains(text(),"管理版")]'
        self.driver.click(_manager_menu_loc)

    def business_guidance_grass_roots(self, org_code) -> None:
        _businessAudit_menu_loc = 'xpath->//span[contains(text(),"业务审核")]'
        _businessGuidance_menu_loc = 'xpath->//div[@class="menu-sub ng-star-inserted"]/ul/li[4]/a'
        _query_org_input_loc = 'xpath->//input[@placeholder="输入统一社会信用代码/单位名称/主管单位查询"]'
        _orgcode_link_loc = f'link->{org_code}'
        self.click_manager()
        self.driver.move_to_element(_businessAudit_menu_loc)  # 悬停在业务审核
        self.driver.click(_businessGuidance_menu_loc)  # 点击业务指导基层
        self.driver.input(_query_org_input_loc, org_code)  # 输入查询统一社会信用代码
        self.driver.click(_orgcode_link_loc)  # 点击统一社会信用代码进入基层单位
        self.driver.switch_to_new_window()

    def upload_attachment(self) -> None:
        """
        上传附件
        """
        _attachment_btn_loc = "xpath->//span[contains(text(),'工资报审附件')]"
        _upload_btn_loc = "xpath->(//button[@class='ant-btn ng-star-inserted'])[1]"
        _upload_file_msg_loc = "xpath->//div/span[contains(text(),'附件示例.png')]"
        _save_attachment_btn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'

        self.click(_attachment_btn_loc)
        self.click(_upload_btn_loc)
        upload_file(datas_path, "附件示例.png")
        assert "附件示例.png" == self.get_text(_upload_file_msg_loc), "上传附件失败."
        self.click(_save_attachment_btn_loc)
