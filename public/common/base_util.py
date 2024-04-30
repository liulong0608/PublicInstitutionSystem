# == Coding: UTF-8 ==
# @Project :        BusinessWageSystem
# @fileName         base_util.py  
# @version          v0.1
# @author           Echo
# @GiteeWarehouse   https://gitee.com/liu-long068/
# @editsession      2023/6/9
# @Software:        PyCharm
# ====/******/=====
import time
import unittest
from config.globalparam import username, password
from public.common import base_page
from config import globalparam
from public.common.base_page import BasePage
from public.common.log import Log
from public.pages import *
from public.common import browser


class BaseUtil(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    driver = None
    logger = None
    login_username = 'id->username'
    login_password = 'id->password'
    verifyCode = 'id->captcha'
    login_btn = 'xpath->//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button'
    asert_text = 'css->.home_personTitle__cQ0jt'

    @classmethod
    def setUpClass(cls):
        cls.logger = Log().get_logger()
        cls.logger.info('############################### START ###############################')
        driver = browser.select_browser()
        cls.driver: BasePage = BasePage(driver)
        cls.driver.max_window()
        cls.driver.open_url(f'{globalparam.env}/login')
        cls.driver.input(cls.login_username, username)
        cls.driver.input(cls.login_password, password)
        cls.driver.input(cls.verifyCode, 'abcd')
        cls.driver.click(cls.login_btn)
        time.sleep(1.5)

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        cls.logger.info('###############################  End  ###############################')
