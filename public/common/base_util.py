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

from config import globalparam
from public.common import browser
from public.common.base_page import BasePage
from public.common.datainfo import get_xls_to_dict
from public.common.log import Log


class BaseUtil(unittest.TestCase):
    """
    基类用于所有testcase
    """

    driver = None
    logger = None
    _login_username_loc = 'id->username'
    _login_password_loc = 'id->password'
    _verifyCode_loc = 'id->captcha'
    _login_btn_loc = 'xpath->//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button'
    _asert_text_loc = 'css->.home_personTitle__cQ0jt'
    _back_btn_loc = 'css->.tool a'
    _hover_quit_btn_loc = 'xpath->(//div[@class="ant-space-item"])[2]'
    _quit_btn_loc = 'css->li.ant-dropdown-menu-item'

    # @classmethod
    def login_control(self, username, password, verifyCode):
        self.driver.input(self._login_username_loc, username)
        self.driver.input(self._login_password_loc, password)
        self.driver.input(self._verifyCode_loc, verifyCode)
        self.driver.click(self._login_btn_loc)
        time.sleep(1.5)

    def setUp(self):
        self.logger = Log().get_logger()
        self.logger.info('############################### START ###############################')
        datas = get_xls_to_dict("test_datas.xlsx", "login")[0]
        driver = browser.select_browser()
        self.driver: BasePage = BasePage(driver)
        self.driver.max_window()
        self.driver.open_url(f'{globalparam.env}/login')
        self.login_control(datas['username'], datas['password'], datas['verifyCode'])

    def tearDown(self):
        self.driver.click(self._back_btn_loc)
        if self.driver.get_url() == f'{globalparam.env}/home':
            self.driver.move_to_element(self._hover_quit_btn_loc)
            self.driver.click(self._quit_btn_loc)
            self.driver.quit()
        else:
            self.logger.error('跳转首页失败')
        self.logger.info('###############################  End  ###############################')

    # @classmethod
    # def setUpClass(cls):
    #     cls.logger = Log().get_logger()
    #     cls.logger.info('############################### START ###############################')
    #     datas = get_xls_to_dict("test_datas.xlsx", "login")[0]
    #     driver = browser.select_browser()
    #     cls.driver: BasePage = BasePage(driver)
    #     cls.driver.max_window()
    #     cls.driver.open_url(f'{globalparam.env}/login')
    #     cls.login_control(datas['username'], datas['password'], datas['verifyCode'])
    #
    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(5)
    #     cls.driver.quit()
    #     cls.logger.info('###############################  End  ###############################')



