# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @version          v0.5
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, InvalidSelectorException, NoSuchElementException
from public.common.log import Log
from config import globalparam

success = "SUCCESS   "
fail = "FAIL   "
logger = Log()


class BasePage(object):
    def __init__(self, browser):
        global driver
        t1 = time.time()
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome" or browser == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('ignore-certificate-errors')
            options.add_argument("--headers")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(chrome_options=options)
        try:
            self.driver = driver
            self.log_debug("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
        except Exception:
            raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                            "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))
        self.wait: WebDriverWait = WebDriverWait(self.driver, timeout=15, poll_frequency=0.8)

    def quit(self):
        if self.driver is not None:
            self.driver.quit()
            self.log_debug("Browser closed.")

    def log_debug(self, msg):
        logger.info(msg)

    def log_error(self, msg):
        logger.error(msg)
        timestamp = str(int(time.time()))  # 使用时间戳作为文件名
        self.take_screenshot(f"FAIL_{timestamp}.png")

    def element_dyeing(self, element) -> None:
        """
        将被操作的元素染色
        :rollback: 是否将元素回滚
        :return: None
        """
        self.driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
                                   element)

    def __wait_element_visible(self, loc):
        """
        Waiting for an element to display.
        Usage:
        driver.element_wait("id->kw",10)
        """
        if "->" not in loc:
            raise ValueError("Invalid positioning syntax. Expected format: 'by->value'")

        by = loc.split("->")[0].strip()
        value = loc.split("->")[1].strip()
        selector_map = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }

        try:
            locator = (selector_map[by], value)
            self.wait.until(EC.visibility_of_element_located(locator))
            self.log_debug("Element {0} is visible".format(loc))
        except TimeoutException:
            self.log_error("Wait element {0} timed out!".format(loc))
            raise TimeoutException('元素等待超时')

    def get_element(self, loc):
        """
        获取页面元素
        :param loc: 元素定位
        :return: 一个元素
        """
        if "->" not in loc:
            raise ValueError("Invalid positioning syntax. Expected format: 'by->value'")

        by, value = loc.split("->")
        by = by.strip()
        value = value.strip()

        selector_map = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }
        try:
            locator = (selector_map[by], value)
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException:
            raise NoSuchElementException(f"Element {loc} not found")

    def get_elements(self, loc) -> list:
        """
        获取一组元素
        :param loc: 元素定位
        :return: 一组元素
        """
        if "->" not in loc:
            raise ValueError("Invalid positioning syntax. Expected format: 'by->value'")

        by, value = loc.split("->")
        by = by.strip()
        value = value.strip()

        selector_map = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }
        try:
            locator = (selector_map[by], value)
            elements = self.driver.find_elements(*locator)
            return elements
        except NoSuchElementException:
            raise NoSuchElementException(f"Element {loc} not found")

    def open(self, url):
        t1 = time.time()
        try:
            self.driver.get(url)
            self.log_debug("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def max_window(self):
        """
        设置最大窗口
        :return:
        """
        t1 = time.time()
        self.driver.maximize_window()
        self.log_debug("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):
        """
        设置窗口的宽高
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.log_debug("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,
                                                                                              wide, high,
                                                                                              time.time() - t1))

    def send_keys(self, loc, value):
        """
        输入值
        :param loc:
        :param value:
        :return:
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            self.__wait_element_visible(loc)
            el.send_keys(value)
            self.log_debug("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                             loc, value,
                                                                                             time.time() - t1))
        except Exception as e:
            self.log_error("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                      loc, value,
                                                                                                      time.time() - t1))
            raise e

    def clear_type(self, loc, value):
        """
        输入框清除并且输入值
        :param loc:
        :param value:
        :return:
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            self.__wait_element_visible(loc)
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(value)
            el.send_keys(Keys.TAB)
            self.log_debug("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                                      loc, value,
                                                                                                      time.time() - t1))
        except Exception as e:
            self.log_error("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                                loc,
                                                                                                                value,
                                                                                                                time.time() - t1))
            raise e

    def click(self, loc):
        """
        点击元素
        :param loc:
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            el = self.get_element(loc)
            el.click()
            self.log_debug("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception as e:
            self.log_error("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise e

    def right_click(self, loc):
        """
        Right click element.

        Usage:
        driver.right_click("id->kw")
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            self.__wait_element_visible(loc)
            ActionChains(self.driver).context_click(el).perform()
            self.log_debug("{0} Right click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def hover_and_click(self, hover_loc, click_loc):
        """
        鼠标悬停并且点击
        :param hover_loc:
        :param click_loc:
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(hover_loc)
            el = self.get_element(hover_loc)
            ActionChains(self.driver).move_to_element(el).perform()
            self.log_debug("{0} Move to element: <{1}>, Spend {2} seconds".format(success, hover_loc, time.time() - t1))
            el = self.get_element(click_loc)
            el.click()
            self.log_debug(
                "{0} Move to element: <{1}> click element: <{2}>, Spend {3} seconds".format(success, hover_loc,
                                                                                            click_loc,
                                                                                            time.time() - t1))
        except Exception as e:
            self.log_error(
                "{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, hover_loc, time.time() - t1))
            raise e

    def double_click(self, loc):
        """
        双击
        :param loc:
        :return:
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            self.__wait_element_visible(loc)
            ActionChains(self.driver).double_click(el).perform()
            self.log_debug("{0} Double click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def drag_and_drop(self, el_loc, ta_loc):
        """
        拖动一个元素到一定的距离，然后放下它.
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(el_loc)
            element = self.get_element(el_loc)
            self.__wait_element_visible(ta_loc)
            target = self.get_element(ta_loc)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            self.log_debug("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                                                                                                          el_loc,
                                                                                                          ta_loc,
                                                                                                          time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                                                                                                         el_loc,
                                                                                                         ta_loc,
                                                                                                         time.time() - t1))
            raise

    def click_linkText(self, value):
        """
        点击链接文本
        :param value: 链接文本值
        :return:
        """
        time.sleep(1)
        t1 = time.time()
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, value).click()
            self.log_debug(
                "{0} Click by LinkText content: {1}, Spend {2} seconds".format(success, value, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to Click by LinkText content: {1}, Spend {2} seconds".format(fail, value, time.time() - t1))
            raise

    def close(self):
        """
        关闭当前窗口
        """
        t1 = time.time()
        self.driver.close()
        self.log_debug("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def refresh(self):
        """
        刷新浏览器页面
        """
        t1 = time
        self.driver.refresh()
        self.log_debug("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def execute_js(self, script):
        """
        执行js脚本代码
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            self.log_debug(
                "{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,
                                                                                                     script,
                                                                                                     time.time() - t1))
            raise

    def get_attribute(self, loc, attribute):
        """
        获取元素属性的值.
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            attr = el.get_attribute(attribute)
            self.log_debug("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                                                                                                       loc, attribute,
                                                                                                       time.time() - t1))
            return attr
        except Exception:
            self.log_error("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                                                                                                                 loc,
                                                                                                                 attribute,
                                                                                                                 time.time() - t1))
            raise

    def get_element_text(self, loc):
        """
        获取元素的文本值
        :param loc: 定位元素
        :return: 元素文本值
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            value = self.get_element(loc).text
            self.log_debug(
                "{0} Get element text element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
            return value
        except Exception as e:
            self.log_error(
                "{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise e

    def get_title(self):
        """
        获取当前窗口标题
        :return:
        """
        t1 = time.time()
        title = self.driver.title
        self.log_debug("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):
        """
        获取当前窗口url
        :return:
        """
        t1 = time.time()
        time.sleep(1)
        url = self.driver.current_url
        self.log_debug("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def __wait(self, secs):
        """
        等待一段时间
        :param secs:
        :return:
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.log_debug("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
                                                                                                   secs,
                                                                                                   time.time() - t1))

    def accept_alert(self):
        """
        接受警告框
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        self.log_debug("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        """
        关闭警告框
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.log_debug("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, loc):
        """
        切换到指定frame
        :param loc: frame的loc
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            iframe_el = self.get_element(loc)
            self.driver.switch_to.frame(iframe_el)
            self.log_debug(
                "{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        """
        切换到默认的frame
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.log_debug("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def open_new_window(self, loc):
        """
        打开新的窗口
        :param loc:
        :return:
        """
        t1 = time.time()
        try:
            original_windows = self.driver.current_window_handle
            el = self.get_element(loc)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.log_debug(
                "{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                                                                                                      loc,
                                                                                                      time.time() - t1))
        except Exception as e:
            self.log_error("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                                                                                                                 loc,
                                                                                                                 time.time() - t1))
            raise e

    def element_exist(self, loc):
        """
        判断元素是否存在，返回结果为真或假判断元素是否存在，返回结果为真或假.
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            self.log_debug("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, loc, time.time() - t1))
            return True
        except TimeoutException:
            self.log_error("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, loc, time.time() - t1))
            return False

    def take_screenshot(self, filename):
        """
        获取当前窗口截图.
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(globalparam.img_path + '\\' + filename)
            self.log_debug("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,
                                                                                                       filename,
                                                                                                       time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,
                                                                                                                 filename,
                                                                                                                 time.time() - t1))
            raise

    def into_new_window(self):
        """
        进入新窗口.
        :return:
        """
        t1 = time.time()
        try:
            current_handle = self.driver.current_window_handle
            all_handles = self.driver.window_handles
            print(all_handles)
            for handle in all_handles:
                if handle != current_handle:
                    # 切换到新窗口
                    self.driver.switch_to.window(handle)
                    break
            self.log_debug("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,
                                                                                                          self.get_title(),
                                                                                                          time.time() - t1))
        except Exception:
            self.log_error("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def input_and_enter(self, loc, value, secs = 0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            ele = self.get_element(loc)
            ele.send_keys(value)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.log_debug(
                "{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                    success, loc, value, secs, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                format(fail, loc, value, secs, time.time() - t1))
            raise

    def htmlSelect(self, select_loc, option_value):
        """
        特殊下拉框控件选择
        :param option_value: 需要选择的元素
        :param select_loc: 下拉框控件元素
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(select_loc)
            self.click(select_loc)
            time.sleep(1)
            # 获取所有下拉值
            select_options = self.driver.find_elements(By.CSS_SELECTOR, 'nz-option-item')
            for select_option in select_options:
                attribute = select_option.get_attribute('title')
                if attribute == option_value:
                    self.click(f'xpath->//nz-option-item[@title="{attribute}"]')
                    break
            self.log_debug(
                "{0}HtmlSelect element <{1}> is selected successfully, Spend {2} seconds".format(success,
                                                                                                 f'xpath->//nz-option-item[@title="{option_value}"]',
                                                                                                 time.time() - t1))
        except Exception as e:
            self.log_error(
                "{0}HtmlSelect element <{1}> not found, Spend {2} seconds".format(fail, option_value, time.time() - t1))
            raise e

    def js_click(self, loc):
        """
        Input a css selecter,use javascript click element.

        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(loc)
        try:
            self.driver.execute_script(js_str)
            self.log_debug(
                "{0} Use javascript click element: {1}, Spend {2} seconds".format(success, js_str, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,
                                                                                                       js_str,
                                                                                                       time.time() - t1))
            raise

    @property
    def origin_driver(self):
        """
        Return the original driver,Can use webdriver API.

        Usage:
        driver.origin_driver
        """
        return self.driver

    def upload_winFile(self, loc, filepath):
        """
        通过Windows系统上传文件
        """
        t1 = time.time()
        try:
            time.sleep(1.5)
            self.get_element(loc).send_keys(filepath)
            time.sleep(3)
            self.log_debug("{0} File uploaded successfully, Spend {1} seconds".format(success, time.time() - t1))
        except Exception as e:
            self.log_error("{0} File uploaded fail, Spend {1} seconds".format(fail, time.time() - t1))
            raise e

    def fuzzy_assert(self, expect, practical_loc):
        """
        模糊断言
        :param expect: 预期结果
        :param practical_loc: 实际结果
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(practical_loc)
            practical = self.get_element_text(practical_loc)
            assert expect in practical
            self.log_debug(
                "{0}Assertion success, expected result 【{1}】, actual result 【{2}】, Spend {3} seconds".format(success,
                                                                                                             expect,
                                                                                                             practical,
                                                                                                             time.time() - t1))
        except Exception:
            logger.error(
                "{0}Assertion failure, expected result 【{1}】, actual result 【{2}】, Spend {3} seconds".format(fail,
                                                                                                             expect,
                                                                                                             practical,
                                                                                                             time.time() - t1))
            raise
        finally:
            timestamp = str(int(time.time()))  # 使用时间戳作为文件名
            self.take_screenshot(f"assertion_{timestamp}.png")

    def assert_equals(self, expect, practical_loc):
        """
        断言
        :param expect: 预期结果
        :param practical_loc: 实际结果
        :return:
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(practical_loc)
            practical = self.get_element_text(practical_loc)
            assert expect == practical
            self.log_debug(
                "{0}Assertion success, expected result 【{1}】, actual result 【{2}】, Spend {3} seconds".format(success,
                                                                                                             expect,
                                                                                                             practical,
                                                                                                             time.time() - t1))
        except AssertionError:
            logger.error(
                "{0}Assertion failure, expected result 【{1}】, actual result 【{2}】, Spend {3} seconds".format(fail,
                                                                                                             expect,
                                                                                                             practical,
                                                                                                             time.time() - t1))
            raise
        finally:
            timestamp = str(int(time.time()))  # 使用时间戳作为文件名
            self.take_screenshot(f"assertion_{timestamp}.png")
