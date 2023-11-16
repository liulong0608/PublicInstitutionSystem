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
from public.common.log import LoguruLogger
from config import globalparam

log = LoguruLogger(stream=True).get_logger()


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
            log.success("Start a new browser: {0}, Spend {1} seconds".format(browser, time.time() - t1))
        except Exception:
            raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                            "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))

    def wait(self, timeout=15, poll=0.8):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)

    @staticmethod
    def get_by_value(loc):
        """"""
        if "->" not in loc:
            raise ValueError("Invalid positioning syntax. Expected format: 'by->value'")
        by = loc.split("->")[0].strip()
        value = loc.split("->")[1].strip()
        locator = (by, value)
        return locator

    def quit(self):
        """
        退出当前窗口
        :return:
        """
        t1 = time.time()
        if self.driver is not None:
            self.driver.quit()
            log.success("Quit current window, Spend {0} seconds".format(time.time() - t1))

    def close(self):
        """
        关闭当前窗口
        :return:
        """
        t1 = time.time()
        self.driver.close()
        log.success("Closed current window, Spend {0} seconds".format(time.time() - t1))

    def element_dyeing(self, element) -> None:
        """
        将被操作的元素染色
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
        pass

    def get_element(self, loc):
        """
        获取页面元素
        :param loc: 元素定位
        :return: 一个元素
        """
        try:
            locator = self.get_by_value(loc)
            return self.wait().until(lambda x: x.find_element(*locator))
        except NoSuchElementException:
            raise NoSuchElementException(f"Element {loc} not found")

    def get_elements(self, loc) -> list:
        """
        获取一组元素
        :param loc: 元素定位
        :return: 一组元素
        """
        try:
            locator = self.get_by_value(loc)
            return self.wait().until(lambda x: x.find_elements(*locator))
        except NoSuchElementException:
            raise NoSuchElementException(f"Element {loc} not found")

    def open(self, url):
        t1 = time.time()
        try:
            self.driver.get(url)
            log.success("Navigated to {0}, Spend {1} seconds".format(url, time.time() - t1))
        except Exception:
            log.error("Unable to load {0}, Spend {1} seconds".format(url, time.time() - t1))
            raise

    def max_window(self):
        """
        设置最大窗口
        :return:
        """
        t1 = time.time()
        self.driver.maximize_window()
        log.success("Set browser window maximized, Spend {0} seconds".format(time.time() - t1))

    def set_window(self, wide, high):
        """
        设置窗口的宽高
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        log.success("Set browser window wide: {0},high: {1}, Spend {2} seconds".format(wide, high, time.time() - t1))

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
            log.success("Typed element: <{0}> content: {1}, Spend {2} seconds".format(loc, value, time.time() - t1))
        except Exception as e:
            log.error(
                "Unable to type element: <{0}> content: {1}, Spend {2} seconds".format(loc, value, time.time() - t1))
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
            log.success(
                "Clear and type element: <{0}> content: {1}, Spend {2} seconds".format(loc, value, time.time() - t1))
        except Exception as e:
            log.error("Unable to clear and type element: <{0}> content: {1}, Spend {2} seconds".format(loc, value,
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
            log.success("Clicked element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
        except Exception as e:
            log.error("Unable to click element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
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
            log.success("Right click element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
        except Exception:
            log.error(
                "Unable to right click element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
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
            log.success("Move to element: <{0}>, Spend {1} seconds".format(hover_loc, time.time() - t1))
            el = self.get_element(click_loc)
            el.click()
            log.success(
                "Move to element: <{0}> click element: <{1}>, Spend {2} seconds".format(hover_loc, click_loc,
                                                                                        time.time() - t1))
        except Exception as e:
            log.error(
                "Unable move to element: <{0}>, Spend {1} seconds".format(hover_loc, time.time() - t1))
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
            log.success("Double click element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
        except Exception:
            log.error(
                "Unable to double click element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
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
            log.success("Drag and drop element: <{0}> to element: <{1}>, Spend {2} seconds".format(el_loc, ta_loc,
                                                                                                   time.time() - t1))
        except Exception:
            log.error(
                "Unable to drag and drop element: <{0}> to element: <{1}>, Spend {2} seconds".format(el_loc, ta_loc,
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
            log.success(
                "Click by LinkText content: {0}, Spend {1} seconds".format(value, time.time() - t1))
        except Exception:
            log.error(
                "Unable to Click by LinkText content: {0}, Spend {1} seconds".format(value, time.time() - t1))
            raise

    def refresh(self):
        """
        刷新浏览器页面
        """
        t1 = time.time()
        self.driver.refresh()
        log.success("Refresh the current page, Spend {0} seconds".format(time.time() - t1))

    def execute_js(self, script):
        """
        执行js脚本代码
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            log.success(
                "Execute javascript utils: {0}, Spend {1} seconds".format(script, time.time() - t1))
        except Exception:
            log.error("Unable to execute javascript utils: {0}, Spend {1} seconds".format(script,
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
            log.success("Get attribute element: <{0}>,attribute: {1}, Spend {2} seconds".format(loc, attribute,
                                                                                                time.time() - t1))
            return attr
        except Exception:
            log.error("Unable to get attribute element: <{0}>,attribute: {1}, Spend {2} seconds".format(loc, attribute,
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
            log.success(
                "Get element text element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
            return value
        except Exception as e:
            log.error(
                "Unable to get element text element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
            raise e

    def get_title(self):
        """
        获取当前窗口标题
        :return:
        """
        t1 = time.time()
        title = self.driver.title
        log.success("Get current window title, Spend {0} seconds".format(time.time() - t1))
        return title

    def get_url(self):
        """
        获取当前窗口url
        :return:
        """
        t1 = time.time()
        time.sleep(1)
        url = self.driver.current_url
        log.success("Get current window url, Spend {0} seconds".format(time.time() - t1))
        return url

    def __wait(self, secs):
        """
        等待一段时间
        :param secs:
        :return:
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        log.success("Set wait all element display in {0} seconds, Spend {1} seconds".format(secs, time.time() - t1))

    def accept_alert(self):
        """
        接受警告框
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        log.success("Accept warning box, Spend {0} seconds".format(time.time() - t1))

    def dismiss_alert(self):
        """
        关闭警告框
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        log.success("Dismisses the alert available, Spend {0} seconds".format(time.time() - t1))

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
            log.success(
                "Switch to frame element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
        except Exception:
            log.error(
                "Unable switch to frame element: <{0}>, Spend {1} seconds".format(loc, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        """
        切换到默认的frame
        :return:
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        log.success("Switch to frame out, Spend {0} seconds".format(time.time() - t1))

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
            log.success(
                "Click element: <{0}> open a new window and swich into, Spend {1} seconds".format(loc,
                                                                                                  time.time() - t1))
        except Exception as e:
            log.error("Failed to open a new window, Spend {0} seconds".format(loc, time.time() - t1))
            raise e

    def element_exist(self, loc):
        """
        判断元素是否存在，返回结果为真或假判断元素是否存在，返回结果为真或假.
        """
        t1 = time.time()
        try:
            self.__wait_element_visible(loc)
            log.success("Element: <{0}> is exist, Spend {1} seconds".format(loc, time.time() - t1))
            return True
        except TimeoutException:
            log.error("Element: <{0}> is not exist, Spend {1} seconds".format(loc, time.time() - t1))
            return False

    def take_screenshot(self, filename):
        """
        获取当前窗口截图.
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(globalparam.img_path + '\\' + filename)
            log.success("Get the current window screenshot,path: {0}, Spend {1} seconds".format(filename,
                                                                                                time.time() - t1))
        except Exception:
            log.error("Unable to get the current window screenshot,path: {0}, Spend {1} seconds".format(filename,
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
            log.success("Switch to the new window,new window's url: {0}, Spend {1} seconds".format(self.get_title(),
                                                                                                   time.time() - t1))
        except Exception:
            log.error("Unable switch to the new window, Spend {0} seconds".format(time.time() - t1))
            raise

    def input_and_enter(self, loc, value, secs=0.5):
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
            log.success(
                "Element <{0}> type content: {1},and sleep {2} seconds,input ENTER key, Spend {3} seconds".format(
                    loc, value, secs, time.time() - t1))
        except Exception:
            log.error(
                "Unable element <{0}> type content: {1},and sleep {2} seconds,input ENTER key, Spend {3} seconds".
                format(loc, value, secs, time.time() - t1))
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
            log.success(
                "HtmlSelect element <{0}> is selected successfully, Spend {1} seconds".format(
                    f'xpath->//nz-option-item[@title="{option_value}"]',
                    time.time() - t1))
        except Exception as e:
            log.error(
                "HtmlSelect element <{0}> not found, Spend {1} seconds".format(option_value, time.time() - t1))
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
            log.success(
                "Use javascript click element: {0}, Spend {1} seconds".format(js_str, time.time() - t1))
        except Exception:
            log.error("Unable to use javascript click element: {0}, Spend {1} seconds".format(js_str,
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
            log.success("File uploaded successfully, Spend {0} seconds".format(time.time() - t1))
        except Exception as e:
            log.error("File uploaded fail, Spend {0} seconds".format(time.time() - t1))
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
            log.success(
                "Assertion success, expected result 【{0}】, actual result 【{1}】, Spend {2} seconds".format(expect,
                                                                                                          practical,
                                                                                                          time.time() - t1))
        except Exception:
            log.error(
                "Assertion failure, expected result 【{0}】, actual result 【{1}】, Spend {2} seconds".format(expect,
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
            log.success(
                "Assertion success, expected result 【{0}】, actual result 【{1}】, Spend {2} seconds".format(expect,
                                                                                                          practical,
                                                                                                          time.time() - t1))
        except AssertionError:
            log.error(
                "Assertion failure, expected result 【{0}】, actual result 【{1}】, Spend {2} seconds".format(expect,
                                                                                                             practical,
                                                                                                             time.time() - t1))
            raise
        finally:
            timestamp = str(int(time.time()))  # 使用时间戳作为文件名
            self.take_screenshot(f"assertion_{timestamp}.png")
