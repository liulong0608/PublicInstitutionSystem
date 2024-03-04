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
from public.common import base_page
from config import globalparam
from public.common.base_page import BasePage
from public.common.log import Log
from public.pages import *
from public.common import browser

login_username = 'id->username'
login_password = 'id->password'
verifyCode = 'id->captcha'
login_btn = 'xpath->//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button'
asert_text = 'css->.home_personTitle__cQ0jt'


class BaseUtil(unittest.TestCase, BasePage):
    """
    The base class is for all testcase.
    """

    def setUp(self):
        self.logger = Log().get_logger()
        self.logger.info('############################### START ###############################')
        self.driver = browser.select_browser()
        self.max_window()
        self.open_url(f'{globalparam.env}/login')
        self.input(login_username, '888')
        self.input(login_password, 'Aa123456')
        self.input(verifyCode, 'abcd')
        self.click(login_btn)
        time.sleep(1.5)

    def tearDown(self):
        time.sleep(5)
        self.quit()
        self.logger.info('###############################  End  ###############################')
