# -*- coding=UTF-8 -*-
# @Project :        base_util.py
# @fileName         checked_regular_performance_level_page.py
# @author           Echo
# @EditTime         2024/5/16
import time
from typing import *

import allure

from config import globalparam
from config.globalparam import datas_path
from public.common.base_page import BasePage
from utils.files_upload import upload_file


class CheckedRegularPerformanceLevelPage(BasePage):
    _manage_btn_loc = "xpath->//div[contains(text(),'管理版')]"
    _performance_manager_loc = "xpath->//span[contains(text(),'绩效管理')]"
    _check_performance_level_loc = "xpath->//span[contains(text(),'核定绩效水平')]"
    _checked_regular_performance_level_loc = "xpath->//span[contains(text(),'核定常规绩效水平')]/ancestor::a"
    _click_add_btn_loc = "xpath->//span[contains(text(),'新增')]/ancestor::button"
    _input_performance_date_loc = "css->.ant-modal-content input"
    _click_determine_btn_loc = "xpath->//span[contains(text(),'确定')]/ancestor::button"
    _input_org_code_loc = "xpath->//input[@placeholder='输入统一社会信用代码、单位名称、主管单位进行查询']"
    _click_choose_btn_loc = "css->.transfer__action:nth-child(2) button:nth-child(8)"
    _click_next_step_btn_loc = "xpath->//span[contains(text(),'下一步')]/ancestor::button"
    _input_performance_amount_loc = "css->.ant-table-tbody tr:nth-child(2) td:nth-child(8) input"
    _click_attachment_loc = "xpath->(//a[@class='ant-btn ant-btn-link ant-btn-sm'])[1]"
    _save_attachment_btn_loc = 'css->div.ant-modal-footer button.ant-btn-primary'
    _click_upload_btn_loc = "xpath->(//button[@class='ant-btn ng-star-inserted'])[1]"
    _click_save_btn_loc = "xpath->//span[contains(text(),'保存')]/ancestor::button"
    _save_msg_loc = "css->.ant-message span"
    _m_input_org_code_loc = "xpath->//input[@formcontrolname='condition']"
    _m_input_performance_date_loc = "xpath->(//lib-date-input[@formcontrolname='year'])[1]/div/nz-input-group/input"
    _m_choose_organization_loc = "xpath->//td[text()='1']/preceding-sibling::*[1]"
    _m_modification_btn_loc = 'xpath->//span[contains(text(),"修改")]/ancestor::button'
    _click_delete_btn_loc = 'xpath->//span[contains(text(),"删除")]/ancestor::button'
    _click_appendix_supplement_loc = 'xpath->(//span[contains(text(),"附件补录")]/ancestor::button)[1]'

    def _swith_to_home(self):
        with allure.step('切换到首页'):
            self.driver.open_url(f'{globalparam.env}/home')

    def _click_manage(self):
        with allure.step('点击管理版'):
            self.driver.click(self._manage_btn_loc)

    def _click_chck_regular_performance_level(self):
        with allure.step('点击核定常规绩效水平'):
            self.driver.move_to_element(self._performance_manager_loc)
            self.driver.move_to_element(self._check_performance_level_loc)
            self.driver.click(self._checked_regular_performance_level_loc)

    def _click_create_performance_level(self):
        with allure.step('点击新增'):
            self.driver.click(self._click_add_btn_loc)

    def _input_performance_date(self, date):
        with allure.step('输入绩效年份'):
            self.driver.clear_and_input(self._input_performance_date_loc, date)

    def _click_determine(self):
        with allure.step('点击确定'):
            self.driver.click(self._click_determine_btn_loc)

    def _input_org_code(self, org_code):
        with allure.step('查询单位'):
            self.driver.input(self._input_org_code_loc, org_code)

    def _choose_organization(self):
        with allure.step('选择单位'):
            self.driver.click(self._click_choose_btn_loc)

    def _click_nextSteps(self):
        with allure.step('点击下一步'):
            self.driver.click(self._click_next_step_btn_loc)

    def _input_performance_amount(self, amount):
        with allure.step('输入绩效金额'):
            self.driver.input(self._input_performance_amount_loc, amount)

    def _upload_attachment(self):
        with allure.step('上传附件'):
            self.driver.upload_attachments()

    def _click_save(self):
        with allure.step('点击保存'):
            self.driver.click(self._click_save_btn_loc)

    def _get_save_msg(self):
        with allure.step('获取保存信息'):
            return self.driver.get_text(self._save_msg_loc)

    def _m_input_org_code(self, org_code):
        with allure.step('查询单位'):
            self.driver.input(self._m_input_org_code_loc, org_code)

    def _m_input_performance_date(self, date):
        with allure.step('输入查询绩效年份'):
            self.driver.clear_and_input(self._m_input_performance_date_loc, date)

    def _m_choose_organization(self):
        with allure.step('勾选单位'):
            self.driver.click(self._m_choose_organization_loc)

    def _m_click_modification_btn(self):
        with allure.step('点击修改按钮'):
            self.driver.click(self._m_modification_btn_loc)

    def _click_delete_btn(self):
        with allure.step('点击删除按钮'):
            self.driver.click(self._click_delete_btn_loc)

    def _determine_delete(self):
        with allure.step('点击确定删除'):
            self.driver.click(self._click_determine_btn_loc)

    def _get_delete_msg(self):
        with allure.step('获取删除信息'):
            return self.driver.get_text('css->.ant-message span')

    def _click_appendix_supplement(self):
        with allure.step('点击附件补录'):
            self.driver.click(self._click_appendix_supplement_loc)

    def checked_regular_performance_level(self, date, org_code, amount):
        self._swith_to_home()
        self._click_manage()
        self._click_chck_regular_performance_level()
        self._click_create_performance_level()
        self._input_performance_date(date)
        self._click_determine()
        self._input_org_code(org_code)
        self._choose_organization()
        self._click_nextSteps()
        self._input_performance_amount(amount)
        self._upload_attachment()
        self._click_save()
        return self._get_save_msg()

    def export_performance_level_list(self):
        pass

    def modification_performance_level(self, org_code, date, amount):
        self._m_input_org_code(org_code)
        self._m_input_performance_date(date)
        self._m_choose_organization()
        self._m_click_modification_btn()
        self._input_performance_amount(amount)
        self._click_save()
        return self._get_save_msg()

    def delete_performance_level(self, org_code, date):
        self._m_input_org_code(org_code)
        self._m_input_performance_date(date)
        self._m_choose_organization()
        self._click_delete_btn()
        self._determine_delete()
        return self._get_delete_msg()

    def appendix_supplement(self, org_code, date):
        """
        附件补录
        """
        self._m_input_org_code(org_code)
        self._m_input_performance_date(date)
        self._m_choose_organization()
        self._click_appendix_supplement()
        self._upload_attachment()
        return self._get_save_msg()

