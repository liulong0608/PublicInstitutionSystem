"""         ==Coding: UTF-8==
**    @Project :        PublicInstitutionSystem
**    @fileName         login_page.py
**    @author           Echo
**    @EditTime         2023/12/11
"""
from typing import *

from public.common.base_page import BasePage


class LoginPage(BasePage):
    login_username = '#username'
    login_password = 'id->password'
    verifyCode = 'id->captcha'
    login_btn = 'xpath->//*[@id="root"]/div/div[2]/div[1]/div/form/div[5]/div/div/div/div/button'
    asert_text = 'css->.home_personTitle__cQ0jt'

    def login(self):
        self.driver.max_window()
        self.driver.open_url('http://192.168.2.194/console/login')
        self.driver.input(self.login_username, '888')
        self.driver.input(self.login_password, 'Aa123456')
        self.driver.input(self.verifyCode, 'abcd')
        self.driver.click(self.login_btn)
