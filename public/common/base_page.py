# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_page.py  
# @version          v0.1
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
from selenium.common.exceptions import TimeoutException
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
            driver = webdriver.Chrome(chrome_options=options)
        try:
            self.driver = driver
            self.log_debug("{0} Start a new browser: {1}, Spend {2} seconds".format(success, browser, time.time() - t1))
        except Exception:
            raise NameError("Not found {0} browser,You can enter 'ie','ff',"
                            "'chrome','RChrome','RIe' or 'RFirefox'.".format(browser))

    def log_debug(self, msg):
        logger.info(msg)

    def log_error(self, msg):
        logger.error(msg)
        timestamp = str(int(time.time()))  # 使用时间戳作为文件名
        self.take_screenshot(f"FAIL_{timestamp}.png")

    def element_wait(self, css, secs=10):
        """
        Waiting for an element to display.
        Usage:
        driver.element_wait("id->kw",10)
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),
                                                      messages)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def get_element(self, css):
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()

        if by == 'id':
            element = self.driver.find_element(By.ID, value)
        elif by == 'name':
            element = self.driver.find_element(By.NAME, value)
        elif by == 'class':
            element = self.driver.find_element(By.CLASS_NAME, value)
        elif by == 'link_text':
            element = self.driver.find_element(By.LINK_TEXT, value)
        elif by == 'xpath':
            element = self.driver.find_element(By.XPATH, value)
        elif by == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, value)
        else:
            raise NameError("请输入正确的目标元素，'id'，'name'，'class'，'link_text'，'xpaht'，'css'")
        return element

    def get_elements(self, css):
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()

        if by == 'id':
            elements = self.driver.find_elements(By.ID, value)
        elif by == 'name':
            elements = self.driver.find_elements(By.NAME, value)
        elif by == 'class':
            elements = self.driver.find_elements(By.CLASS_NAME, value)
        elif by == 'link_text':
            elements = self.driver.find_elements(By.LINK_TEXT, value)
        elif by == 'xpath':
            elements = self.driver.find_elements(By.XPATH, value)
        elif by == 'css':
            elements = self.driver.find_elements(By.CSS_SELECTOR, value)
        else:
            raise NameError("请输入正确的目标元素，'id'，'name'，'class'，'link_text'，'xpaht'，'css'")
        return elements

    def open(self, url):
        t1 = time.time()
        try:
            self.driver.get(url)
            self.log_debug("{0} Navigated to {1}, Spend {2} seconds".format(success, url, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to load {1}, Spend {2} seconds".format(fail, url, time.time() - t1))
            raise

    def max_window(self):
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

    def send_keys(self, css, text):
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            self.log_debug("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                             css, text,
                                                                                             time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                      css, text,
                                                                                                      time.time() - t1))
            raise

    def clear_type(self, css, text):
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(text)
            el.send_keys(Keys.TAB)
            self.log_debug("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                                                                                                      css, text,
                                                                                                      time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                                                                                                                css,
                                                                                                                text,
                                                                                                                time.time() - t1))
            raise

    def click(self, css):
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.click()
            self.log_debug("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.log_error("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def right_click(self, css):
        """
        Right click element.

        Usage:
        driver.right_click("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).context_click(el).perform()
            self.log_debug("{0} Right click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def move_to_element(self, css):
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).move_to_element(el).perform()
            self.log_debug("{0} Move to element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.log_error("{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def hover_and_click(self, hover_loc, click_loc):
        self.move_to_element(hover_loc)
        self.element_wait(click_loc)
        el = self.get_element(click_loc)
        el.click()

    def double_click(self, css):
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            ActionChains(self.driver).double_click(el).perform()
            self.log_debug("{0} Double click element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def drag_and_drop(self, el_css, ta_css):
        """
        拖动一个元素到一定的距离，然后放下它.
        """
        t1 = time.time()
        try:
            self.element_wait(el_css)
            element = self.get_element(el_css)
            self.element_wait(ta_css)
            target = self.get_element(ta_css)
            ActionChains(driver).drag_and_drop(element, target).perform()
            self.log_debug("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,
                                                                                                          el_css,
                                                                                                          ta_css,
                                                                                                          time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,
                                                                                                         el_css,
                                                                                                         ta_css,
                                                                                                         time.time() - t1))
            raise

    def click_linkText(self, text):
        time.sleep(1)
        t1 = time.time()
        try:
            self.driver.find_element(By.PARTIAL_LINK_TEXT, text).click()
            self.log_debug(
                "{0} Click by LinkText content: {1}, Spend {2} seconds".format(success, text, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable to Click by LinkText content: {1}, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise

    def close(self):
        """
        关闭当前窗口
        """
        t1 = time.time()
        self.driver.close()
        self.log_debug("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):
        """
        关闭浏览器实例
        """
        t1 = time.time()
        self.driver.quit()
        self.log_debug("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

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

    def get_attribute(self, css, attribute):
        """
        获取元素属性的值.
        """
        t1 = time.time()
        try:
            el = self.get_element(css)
            attr = el.get_attribute(attribute)
            self.log_debug("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,
                                                                                                       css, attribute,
                                                                                                       time.time() - t1))
            return attr
        except Exception:
            self.log_error("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,
                                                                                                                 css,
                                                                                                                 attribute,
                                                                                                                 time.time() - t1))
            raise

    def get_text(self, css):
        t1 = time.time()
        try:
            self.element_wait(css)
            text = self.get_element(css).text
            self.log_debug(
                "{0} Get element text element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
            return text
        except Exception:
            self.log_error(
                "{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def get_title(self):
        t1 = time.time()
        title = self.driver.title
        self.log_debug("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):
        t1 = time.time()
        time.sleep(1)
        url = self.driver.current_url
        self.log_debug("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def wait(self, secs):
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        self.log_debug("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,
                                                                                                   secs,
                                                                                                   time.time() - t1))

    def accept_alert(self):
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        self.log_debug("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        self.log_debug("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, css):
        t1 = time.time()
        try:
            self.element_wait(css)
            iframe_el = self.get_element(css)
            self.driver.switch_to.frame(iframe_el)
            self.log_debug(
                "{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, css, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        t1 = time.time()
        self.driver.switch_to.default_content()
        self.log_debug("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def open_new_window(self, css):
        t1 = time.time()
        try:
            original_windows = self.driver.current_window_handle
            el = self.get_element(css)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            self.log_debug(
                "{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,
                                                                                                      css,
                                                                                                      time.time() - t1))
        except Exception:
            self.log_error("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,
                                                                                                                 css,
                                                                                                                 time.time() - t1))
            raise

    def element_exist(self, css):
        """
        判断元素是否存在，返回结果为真或假判断元素是否存在，返回结果为真或假.
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            self.log_debug("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, css, time.time() - t1))
            return True
        except TimeoutException:
            self.log_error("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, css, time.time() - t1))
            return False

    def take_screenshot(self, filename):
        """
        获取当前窗口截图.
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(globalparam.img_path+'\\'+filename)
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

    def type_and_enter(self, css, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.

        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            ele = self.get_element(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            self.log_debug(
                "{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(
                    success, css, text, secs, time.time() - t1))
        except Exception:
            self.log_error(
                "{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".
                format(fail, css, text, secs, time.time() - t1))
            raise

    def htmlSelect(self, select_css, value_css):
        """
        特殊下拉框控件选择
        :param value_css: 需要选择的元素
        :param select_css: 下拉框控件元素
        :return:
        """
        t1 = time.time()
        try:
            self.click(select_css)
            time.sleep(1)
            self.click(value_css)
            self.log_debug(
                "{0}HtmlSelect element <{1}> is selected successfully, Spend {2} seconds".format(success, value_css,
                                                                                                 time.time() - t1))
        except Exception:
            self.log_error(
                "{0}HtmlSelect element <{1}> not found, Spend {2} seconds".format(fail, value_css, time.time() - t1))
            raise

    def js_click(self, css):
        """
        Input a css selecter,use javascript click element.

        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(css)
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

    def upload_winFile(self, css, filepath):
        """
        通过Windows系统上传文件
        """
        t1 = time.time()
        try:
            self.send_keys(css, filepath)
            time.sleep(3)
            self.log_debug("{0} File uploaded successfully, Spend {1} seconds".format(success, time.time() - t1))
        except Exception:
            self.log_error("{0} File uploaded fail, Spend {1} seconds".format(fail, time.time() - t1))
            raise
        finally:
            self.take_screenshot("assertion_文件上传.png")

    def fuzzy_assert(self, expect, practical_loc, **kwargs):
        """ 模糊断言 """
        t1 = time.time()
        try:
            time.sleep(0.5)
            practical = self.get_text(practical_loc)
            assert expect in practical
            # self.get_img(kwargs)
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

    def assert_equals(self, expect, practical_loc, **kwargs):
        t1 = time.time()
        try:
            time.sleep(0.5)
            practical = self.get_text(practical_loc)
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
