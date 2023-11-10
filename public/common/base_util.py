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
from public.common.log import Log
from public.pages import *


class BaseUtil(unittest.TestCase):
    """
    The base class is for all testcase.
    """

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.driver = base_page.BasePage(globalparam.browser)
        self.driver.max_window()
        self.driver.open('http://192.168.2.194/console/login')
        self.driver.send_keys(login_username, '3men0001')
        self.driver.send_keys(login_password, 'Aa123456')
        self.driver.send_keys(verifyCode, 'abcd')
        self.driver.click(login_btn)
        time.sleep(1.5)

    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
