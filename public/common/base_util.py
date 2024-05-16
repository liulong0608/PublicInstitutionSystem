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

import pytest

from config import globalparam
from public.common import browser
from public.common.base_page import BasePage
from public.common.datainfo import get_xls_to_dict
from public.common.log import Log


class BaseUtil:
    """
    基类用于所有testcase
    """

    driver = None
    logger = None
    _login_username_loc = 'id->username'
    _login_password_loc = 'id->password'
    _verifyCode_loc = 'id->captcha'
    _login_btn_loc = 'xpath->//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button'
    _fail_msg_loc = 'xpath->//div[@class="login_loginCont__wmf1i"]/span'
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

    @pytest.fixture(scope="class", autouse=True)
    def setup_class_method(self):
        self.logger = Log().get_logger()
        self.logger.info('############################### START ###############################')
        datas = get_xls_to_dict("test_datas.xlsx", "login")[0]
        driver = browser.select_browser()
        self.driver: BasePage = BasePage(driver)
        self.driver.max_window()
        self.driver.open_url(f'{globalparam.env}/login')
        self.login_control(datas['username'], datas['password'], datas['verifyCode'])

    @pytest.fixture(scope="class", autouse=True)
    def teardown_class_method(self):
        if self.driver.element_exists(self._back_btn_loc):
            self.driver.click(self._back_btn_loc)
        if self.driver.get_url() == f'{globalparam.env}/home':
            self.driver.move_to_element(self._hover_quit_btn_loc)
            self.driver.click(self._quit_btn_loc)
            self.driver.quit()
        else:
            self.logger.error('跳转首页失败')
        self.logger.info('###############################  End  ###############################')

    def get_cookie(self):
        driver = browser.select_browser()
        self.driver: BasePage = BasePage(driver)
        self.driver.open_url(f'{globalparam.env}/login')
        self.login_control('qyqzs', 'Aa123456', '123456')
        time.sleep(3)
        cookies = self.driver.get_cookie()
        return cookies

    def open_new_url(self):
        cookie_dict = self.get_cookie()
        self.driver.open_url(f'http://192.168.2.209/test_admin?token={cookie_dict[0]['value']}')
        time.sleep(30)





