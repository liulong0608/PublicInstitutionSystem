# -*- coding: UTF-8 -*-
"""
**    @Project :        PublicInstitutionSystem
**    @fileName         personnel_reduction_page.py
**    @author           Echo
**    @EditTime         2024/4/2
"""
from typing import *

import allure

from public.common.base_page import BasePage


class PersonnelReductionPage(BasePage):
    """人员减少"""
    _add_decrease_loc = "xpath->//span[contains(text(),'人员新增减少')]"
    _personnel_reduction_loc = "xpath->//a[@href='/test_bases/personnel/reduce-staff']"
    _off_choice_btn_loc = "xpath->//span[contains(text(),'关闭')]"
    _input_stopPayTime_loc = "xpath->//input[@placeholder='请选择日期']"
    _select_reductionType_loc = "xpath->//nz-select[@formcontrolname='changeTypeId']"
    _save_btn_loc = "xpath->//span[contains(text(),'保存')]"
    _ruduct_success_msg_loc = "css->.ant-modal-confirm-body span.ng-star-inserted"
    _ruduct_determine_success_msg_loc = "xpath->//span[contains(text(),'确定')]"

    def _swith_to_basic_unit(self, org_code):
        """
        进入基层单位
        """
        with allure.step("进入基层单位"):
            self.business_guidance_grass_roots(org_code)

    def _switch_to_personnel_reduction(self):
        """
        进入人员减少界面
        """
        with allure.step("进入人员减少界面"):
            self.driver.move_to_element(self._add_decrease_loc)
            self.driver.click(self._personnel_reduction_loc)

    def _select_personnel_reduction(self):
        """
        选择人员减少
        """
        with allure.step("选择人员减少"):
            self.driver.click(self._off_choice_btn_loc)

    def _input_stopPayTime(self, stopPayTime):
        """
        输入止薪时间
        """
        with allure.step("输入止薪时间"):
            self.driver.clear_and_input(self._input_stopPayTime_loc, stopPayTime)

    def _select_reductionType(self, reductionType):
        """
        选择减少类型
        """
        with allure.step("选择减少类型"):
            self.driver.htmlSelect(self._select_reductionType_loc, reductionType)

    def upload_change_attachment(self) -> None:
        with allure.step("上传附件"):
            self.upload_attachment()

    def _save_change_btn(self):
        """
        保存
        """
        with allure.step("保存"):
            self.driver.click(self._save_btn_loc)

    def _get_ruduct_msg(self):
        """
        获取减少成功提示
        """
        with allure.step("获取减少成功提示"):
            return self.driver.get_text(self._ruduct_success_msg_loc)

    def _click_determine_btn(self):
        """
        点击确定
        """
        with allure.step("点击确定"):
            self.driver.click(self._ruduct_determine_success_msg_loc)

    def personnel_reduction(self, org_code, qx_date, reductionType):
        """
        人员减少
        """
        self._swith_to_basic_unit(org_code)
        self._switch_to_personnel_reduction()
        self._select_personnel_reduction()
        self._input_stopPayTime(qx_date)
        self._select_reductionType(reductionType)
        self.upload_change_attachment()
        self._save_change_btn()
        msg = self._get_ruduct_msg()
        self._click_determine_btn()
        return msg
